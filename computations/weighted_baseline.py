#!/usr/bin/env python3
"""Exact, dependency-free checks for the (1,1,2,3) starting stratum.

The checks concern specified numerical data, the diagonal quantum family,
its diagonal Zhang twists, and a nonrealizable pure-jump-one numerical example.
They are not an AS-regularity test for an
arbitrary relation tuple and do not constitute a classification.

Run from the repository root:
    python3 computations/weighted_baseline.py
Regenerate the retained mathematical certificate:
    python3 computations/weighted_baseline.py --write
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path


WEIGHTS = (1, 1, 2, 3)
PAIRS = tuple(combinations(range(4), 2))
PARAMETERS = tuple(f"q{i}{j}" for i, j in PAIRS)
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
MAX_WEIGHT = 24
ZERO_MONOMIAL = (0,) * len(PAIRS)


def multiply_bivariate(left, right, bound=None):
    result = Counter()
    for (p, n), a in left.items():
        for (q, m), b in right.items():
            if bound is None or n + m <= bound:
                result[p + q, n + m] += a * b
    return {key: value for key, value in result.items() if value}


def denominator_and_betti():
    denominator = {(0, 0): 1}
    for weight in WEIGHTS:
        denominator = multiply_bivariate(
            denominator, {(0, 0): 1, (1, weight): -1}
        )
    betti = [sorted(sum(WEIGHTS[i] for i in subset)
                    for subset in combinations(range(4), degree))
             for degree in range(5)]
    euler = Counter()
    for degree, shifts in enumerate(betti):
        for shift in shifts:
            euler[degree, shift] += (-1) ** degree
    assert denominator == dict(euler)
    assert betti == [[0], [1, 1, 2, 3], [2, 3, 3, 4, 4, 5],
                     [4, 5, 6, 6], [7]]
    for degree in range(5):
        assert sorted(7 - n for n in betti[degree]) == betti[4 - degree]
    return denominator, betti


def hilbert_coefficients(denominator):
    # Product of four geometric series, retaining word length and weight.
    coefficients = {(0, 0): 1}
    for weight in WEIGHTS:
        factor = {(exponent, weight * exponent): 1
                  for exponent in range(MAX_WEIGHT // weight + 1)}
        coefficients = multiply_bivariate(coefficients, factor, MAX_WEIGHT)

    # Independent count of exponent vectors of ordered monomials.
    direct = Counter()
    bounds = [range(MAX_WEIGHT // weight + 1) for weight in WEIGHTS]
    for exponents in product(*bounds):
        weight = sum(a * w for a, w in zip(exponents, WEIGHTS))
        if weight <= MAX_WEIGHT:
            direct[sum(exponents), weight] += 1
    assert coefficients == dict(direct)
    assert multiply_bivariate(denominator, coefficients, MAX_WEIGHT) == {(0, 0): 1}

    hilbert = [sum(value for (length, weight), value in coefficients.items()
                   if weight == n) for n in range(MAX_WEIGHT + 1)]
    # Third count: choose the weight-2 and weight-3 exponents, then there
    # are n-2*c-3*d+1 ways to distribute the remaining weight to x0,x1.
    independent = [sum(n - 2 * c - 3 * d + 1
                       for d in range(n // 3 + 1)
                       for c in range((n - 3 * d) // 2 + 1))
                   for n in range(MAX_WEIGHT + 1)]
    assert hilbert == independent
    univariate = Counter()
    for (length, weight), value in denominator.items():
        univariate[weight] += value
    univariate = {weight: value for weight, value in univariate.items() if value}
    assert univariate == {0: 1, 1: -2, 3: 1, 4: 1, 6: -2, 7: 1}
    return hilbert, univariate


def presentation_data(betti):
    tensor_dimensions = Counter(a + b for a in WEIGHTS for b in WEIGHTS)
    relation_dimensions = Counter(betti[2])
    assert tensor_dimensions == {2: 4, 3: 4, 4: 5, 5: 2, 6: 1}
    rows = []
    for weight in sorted(tensor_dimensions):
        ambient = tensor_dimensions[weight]
        relations = relation_dimensions.get(weight, 0)
        rows.append({"weight": weight, "tensor_dimension": ambient,
                     "relation_dimension": relations,
                     "grassmannian_dimension": relations * (ambient - relations)})
    one_vertex = sum(row["grassmannian_dimension"] for row in rows)
    gauge_one_vertex = sum(multiplicity ** 2
                           for multiplicity in Counter(WEIGHTS).values())
    assert one_vertex == 14 and gauge_one_vertex == 6
    return {"by_weight": rows, "one_vertex_relation_parameter_dimension": one_vertex,
            "seven_vertex_relation_parameter_dimension": 7 * one_vertex,
            "seven_vertex_linear_generator_group_dimension": 7 * gauge_one_vertex,
            "interpretation": "Dimensions of presentation data only; no moduli dimension is asserted."}


def add_monomials(left, right):
    return tuple(a + b for a, b in zip(left, right))


def scalar_monomial(exponent, monomial):
    return tuple(exponent * a for a in monomial)


def one_parameter(index):
    return tuple(int(i == index) for i in range(len(PAIRS)))


def monomial_text(monomial):
    numerator, denominator = [], []
    for name, exponent in zip(PARAMETERS, monomial):
        if exponent:
            target = numerator if exponent > 0 else denominator
            power = abs(exponent)
            target.append(name if power == 1 else f"{name}^{power}")
    top = "*".join(numerator) or "1"
    return top if not denominator else f"({top})/({'*'.join(denominator)})"


def reduce_word(word, side):
    """Reduce by x_j x_i -> q_ij x_i x_j (j>i), exactly."""
    word = list(word)
    coefficient = ZERO_MONOMIAL
    swaps = 0
    while True:
        inversions = [position for position in range(len(word) - 1)
                      if word[position] > word[position + 1]]
        if not inversions:
            return tuple(word), coefficient, swaps
        position = inversions[0] if side == "left" else inversions[-1]
        high, low = word[position:position + 2]
        coefficient = add_monomials(coefficient,
                                    one_parameter(PAIR_INDEX[low, high]))
        word[position], word[position + 1] = low, high
        swaps += 1


def independent_inversion_coefficient(word):
    result = [0] * len(PAIRS)
    for position, high in enumerate(word):
        for low in word[position + 1:]:
            if high > low:
                result[PAIR_INDEX[low, high]] += 1
    return tuple(result)


def quantum_overlap_data():
    overlaps = []
    for i, j, k in combinations(range(4), 3):
        word = (k, j, i)
        left_word, left_coefficient, left_swaps = reduce_word(word, "left")
        right_word, right_coefficient, right_swaps = reduce_word(word, "right")
        expected = independent_inversion_coefficient(word)
        assert left_word == right_word == (i, j, k)
        assert left_coefficient == right_coefficient == expected
        assert left_swaps == right_swaps == 3
        overlaps.append({"overlap": list(word), "normal_word": list(left_word),
                         "coefficient_exponents": list(left_coefficient),
                         "coefficient": monomial_text(left_coefficient)})
    assert len(overlaps) == 4
    return {"relations": "x_j*x_i = q_ij*x_i*x_j for i<j, all q_ij nonzero",
            "parameter_order": list(PARAMETERS), "critical_overlaps": overlaps,
            "termination": "Every rule strictly decreases the inversion count of a word.",
            "coverage": "These are all overlapping ambiguities; there are no inclusion ambiguities. Disjoint replacements commute.",
            "scope": "Exact symbolic Diamond-lemma check for the diagonal family; AS regularity uses its separate proof/reference."}


def ore_pbw_data():
    """Symbolic critical-pair check over Z[a,b] for the additive Ore chart."""
    # A term is (word, a exponent, b exponent, integer coefficient).
    rules = {
        (1, 0): [((0, 1), 0, 0, 1)],
        (2, 0): [((0, 2), 0, 0, 1)],
        (2, 1): [((1, 2), 0, 0, 1)],
        (3, 0): [((0, 3), 0, 0, 1), ((2, 2), 1, 0, 1)],
        (3, 1): [((1, 3), 0, 0, 1), ((2, 2), 0, 1, 1)],
        (3, 2): [((2, 3), 0, 0, 1)],
    }
    for leading, terms in rules.items():
        for replacement, a, b, coefficient in terms:
            assert len(replacement) == len(leading)
            assert replacement < leading  # degree-lex descent, t>z>y>x
            assert sum(WEIGHTS[i] for i in replacement) == sum(WEIGHTS[i] for i in leading)

    @lru_cache(None)
    def normal_form(word, side):
        positions = [position for position in range(len(word) - 1)
                     if word[position:position + 2] in rules]
        if not positions:
            return {(word, 0, 0): 1}
        position = positions[0] if side == "left" else positions[-1]
        result = Counter()
        for replacement, a, b, coefficient in rules[word[position:position + 2]]:
            new_word = word[:position] + replacement + word[position + 2:]
            for (ordered, c, d), scalar in normal_form(new_word, side).items():
                result[ordered, a + c, b + d] += coefficient * scalar
        return {key: value for key, value in result.items() if value}

    expected = {
        (2, 1, 0): {((0, 1, 2), 0, 0): 1},
        (3, 1, 0): {((0, 1, 3), 0, 0): 1,
                    ((1, 2, 2), 1, 0): 1, ((0, 2, 2), 0, 1): 1},
        (3, 2, 0): {((0, 2, 3), 0, 0): 1, ((2, 2, 2), 1, 0): 1},
        (3, 2, 1): {((1, 2, 3), 0, 0): 1, ((2, 2, 2), 0, 1): 1},
    }
    overlaps = []
    for i, j, k in combinations(range(4), 3):
        word = (k, j, i)
        left = normal_form(word, "left")
        right = normal_form(word, "right")
        assert left == right == expected[word]
        overlaps.append({"overlap": list(word), "normal_form": [
            {"word": list(ordered), "a_exponent": a, "b_exponent": b,
             "coefficient": coefficient}
            for (ordered, a, b), coefficient in sorted(left.items())]})

    # Form r_tx=tx-xt-a*zz and r_ty=ty-yt-b*zz directly from the
    # rewriting rules. Projection to the one-dimensional zz summand
    # has coordinate polynomials -a,-b, and hence vanishes iff a=b=0.
    projected = []
    for leading in [(3, 0), (3, 1)]:
        projection = {(a, b): -coefficient
                      for replacement, a, b, coefficient in rules[leading]
                      if replacement == (2, 2)}
        projected.append(projection)
    assert projected == [{(1, 0): -1}, {(0, 1): -1}]
    return {"generator_order": ["x", "y", "z", "t"],
            "relations": ["yx=xy", "zx=xz", "zy=yz",
                          "tx=xt+a*zz", "ty=yt+b*zz", "tz=zt"],
            "coefficient_ring": "Z[a,b]",
            "critical_overlaps": overlaps,
            "termination": "Every replacement strictly decreases degree-lex order with t>z>y>x and preserves word length.",
            "zz_projection": {"relation_basis": ["tx-xt-a*zz", "ty-yt-b*zz"],
                              "coordinate_matrix": [["-a", "-b"]],
                              "rank_zero_locus": "a=b=0", "rank_elsewhere": 1},
            "scope": "All critical ambiguities vanish identically for every a,b. AS regularity and classification use the separate Ore/duality and isomorphism arguments."}


def matrix_rank(matrix):
    work = [[Fraction(entry) for entry in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scalar = work[rank][column]
        work[rank] = [entry / scalar for entry in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                scalar = work[row][column]
                work[row] = [a - scalar * b for a, b in zip(work[row], work[rank])]
        rank += 1
        if rank == len(work):
            break
    return rank


def twist_data():
    action_matrix = []
    for i, j in PAIRS:
        row = [0] * 4
        row[i], row[j] = WEIGHTS[j], -WEIGHTS[i]
        action_matrix.append(row)
    invariant_matrix = [[2, -1, 0, 1, 0, 0],
                        [3, 0, -1, 0, 1, 0],
                        [0, 3, -2, 0, 0, 1]]
    assert matrix_rank(action_matrix) == matrix_rank(invariant_matrix) == 3
    for invariant in invariant_matrix:
        assert all(sum(invariant[row] * action_matrix[row][column]
                       for row in range(6)) == 0 for column in range(4))
    assert all(sum(entry * weight for entry, weight in zip(row, WEIGHTS)) == 0
               for row in action_matrix)

    # With lambda_0=1 and lambda_j=q_0j, the first three parameters become
    # 1 and the last three become precisely the displayed invariants.
    substitutions = [ZERO_MONOMIAL] + [one_parameter(PAIR_INDEX[0, j])
                                       for j in range(1, 4)]
    normalized = []
    for index, (i, j) in enumerate(PAIRS):
        transformed = add_monomials(one_parameter(index),
                                   scalar_monomial(WEIGHTS[j], substitutions[i]))
        transformed = add_monomials(transformed,
                                   scalar_monomial(-WEIGHTS[i], substitutions[j]))
        normalized.append(transformed)
    assert normalized[:3] == [ZERO_MONOMIAL] * 3
    assert normalized[3:] == [tuple(row) for row in invariant_matrix]

    # The last 3 columns form I_3.  Any integral kernel vector is fixed
    # by its last 3 entries: the lambda_1,lambda_2,lambda_3 equations force
    # (a01,a02,a03)=(2*a12+3*a13, -a12+3*a23, -a13-2*a23).
    assert [row[3:] for row in invariant_matrix] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return {"convention": "a star b = a*sigma^(weight(a))(b); sigma(x_i)=lambda_i*x_i",
            "parameter_transformation": "q'_ij=q_ij*lambda_i^(w_j)/lambda_j^(w_i)",
            "parameter_order": list(PARAMETERS),
            "action_exponent_matrix": action_matrix,
            "action_rank_over_Q": 3,
            "action_kernel": "(lambda_0,lambda_1,lambda_2,lambda_3)=(s,s,s^2,s^3)",
            "invariant_exponent_matrix": invariant_matrix,
            "invariants": [monomial_text(tuple(row)) for row in invariant_matrix],
            "normalization": "lambda_0=1, lambda_j=q_0j for j=1,2,3",
            "normalized_parameters": [monomial_text(row) for row in normalized],
            "integral_kernel_basis": True,
            "scope": "Complete invariant for this diagonal twist action on the parameter torus only. Further indexed-isomorphism identifications are not classified here."}


def pure_jump_one_obstruction():
    """Reproduce the note's numerical example, not an algebra realization."""
    ranks = (0, 0, 0, 1, 1, 2, 1)
    rows = []
    for start in range(7):
        row = [1, 2]
        for length in range(2, 16):
            row.append(2 * row[-1] - ranks[(start + length - 2) % 7] * row[-2])
        assert min(row) >= 0 and row[-2:] == [0, 0]
        while row[-3:] == [0, 0, 0]:
            row.pop()
        rows.append(row)

    monodromy = [[1, 0], [0, 1]]
    for rank in ranks:
        transfer = [[2, -rank], [1, 0]]
        monodromy = [[sum(transfer[i][k] * monodromy[k][j] for k in range(2))
                      for j in range(2)] for i in range(2)]
    assert monodromy == [[0, 0], [8, 0]]
    assert all(not (ranks[i] == ranks[(i + 3) % 7] == 0) for i in range(7))
    assert all(not (ranks[i] == ranks[(i + d) % 7] == 2)
               for i in range(7) for d in (2, 3))
    return {
        "ranks": list(ranks),
        "recurrence": "b[i,0]=1, b[i,1]=2; b[i,n]=2*b[i,n-1]-a[(i+n-2)%7]*b[i,n-2]",
        "rows_through_first_consecutive_zeros": rows,
        "monodromy": monodromy,
        "scope": "Nonnegative Euler data only. This is not realized by a quadratic pure-jump-one algebra with exact length-two simple resolutions: the tensor-chain argument in idx:thm:outer-relation-ranks rules it out. It is not an AS-regular example.",
    }


def build_certificate():
    denominator, betti = denominator_and_betti()
    hilbert, univariate = hilbert_coefficients(denominator)
    return {"schema": "nc-p1123-weighted-baseline-v2", "date": "2026-11-19", "weights": list(WEIGHTS),
            "arithmetic": "Exact integers, rational elimination, and Laurent-monomial exponent vectors; no floating point.",
            "standard_resolution_shifts": betti,
            "bivariate_euler_polynomial": [
                {"word_length": length, "weight": weight, "coefficient": coefficient}
                for (length, weight), coefficient in sorted(denominator.items())],
            "weighted_euler_polynomial": [
                {"weight": weight, "coefficient": coefficient}
                for weight, coefficient in sorted(univariate.items())],
            "hilbert_coefficients_weight_0_through_24": hilbert,
            "bivariate_inverse_verified_through_weight": MAX_WEIGHT,
            "presentation": presentation_data(betti),
            "diagonal_quantum_pbw": quantum_overlap_data(),
            "additive_ore_pbw": ore_pbw_data(),
            "diagonal_twist": twist_data(),
            "pure_jump_one_obstruction": pure_jump_one_obstruction(),
            "limitations": [
                "The standard resolution shifts are specified data, not deduced from the Hilbert series.",
                "A finite Hilbert check does not prove exactness of an arbitrary Koszul complex.",
                "The dimension 98 is a presentation-parameter dimension, not an AS locus or moduli dimension.",
                "No exhaustive classification, non-periodic example, or novelty claim is certified."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="replace the current mathematical certificate")
    parser.add_argument("--certificate", type=Path,
                        default=Path(__file__).with_name("baseline_certificate.json"))
    args = parser.parse_args()
    certificate = build_certificate()
    if args.write:
        args.certificate.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        action = "wrote"
    else:
        retained = json.loads(args.certificate.read_text(encoding="utf-8"))
        if retained != certificate:
            raise SystemExit("Certificate differs; inspect the mathematical change before using --write.")
        action = "matched"
    print(f"PASS: exact weighted Hilbert/Euler, quantum and Ore PBW overlaps, diagonal twists, and the nonrealizable numerical recurrence; {action} {args.certificate.name}.")


if __name__ == "__main__":
    main()
