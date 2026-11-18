#!/usr/bin/env python3
"""Exact finite elimination of the mixed relation-rank candidates.

2026-11-19 / v1.  Python standard library only; no floating point.

The mathematical argument supplies necessary conditions on the seven
integers delta_i = r_3(i)-2.  This program exhausts those finite conditions;
it does not construct an AS-regular algebra or test arbitrary relations for
AS regularity.  See the proof in papers/nc-p1123.tex for the implications
from AS regularity to these necessary rank conditions.

Run from the repository root:
    python3 computations/verify_mixed_ranks.py
Regenerate the current certificate from the same exhaustive computation:
    python3 computations/verify_mixed_ranks.py --write

S_ij = 1 exactly when j = i+1 modulo 7, D = diag(delta), and
    C = 2I - 2(S + S^-1) + S^3 + S^4 + D S^3 + S^4 D.
This is the symmetric integer matrix P(1,1).  Among the 890 tuples with
delta_i in {-2,-1,0,1,2}, sum(delta)=0, and delta_i+delta_{i+1} <= 1,
the sole tuple satisfying det(C)=0 is delta=0.
"""

from __future__ import annotations

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path


PERIOD = 7
DELTA_VALUES = (-2, -1, 0, 1, 2)
CERTIFICATE_PATH = Path(__file__).with_name("mixed_ranks_certificate.json")


def determinant_bareiss(matrix: list[list[int]]) -> int:
    """Integer determinant with row pivoting and checked exact divisions."""
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("The determinant requires a square matrix.")
    if size == 0:
        return 1
    entries = [row[:] for row in matrix]
    sign = 1
    previous_pivot = 1
    for column in range(size - 1):
        pivot_row = next((row for row in range(column, size)
                          if entries[row][column] != 0), None)
        if pivot_row is None:
            return 0
        if pivot_row != column:
            entries[column], entries[pivot_row] = entries[pivot_row], entries[column]
            sign = -sign
        pivot = entries[column][column]
        for row in range(column + 1, size):
            for target in range(column + 1, size):
                numerator = (pivot * entries[row][target]
                             - entries[row][column] * entries[column][target])
                quotient, remainder = divmod(numerator, previous_pivot)
                if remainder:
                    raise ArithmeticError("A Bareiss division was not exact.")
                entries[row][target] = quotient
            entries[row][column] = 0
        previous_pivot = pivot
    return sign * entries[-1][-1]


def rank_matrix(delta: tuple[int, ...]) -> list[list[int]]:
    """Build C with the stated forward-shift convention, without rounding."""
    if len(delta) != PERIOD:
        raise ValueError("Exactly seven delta entries are required.")
    matrix = [[0] * PERIOD for _ in range(PERIOD)]
    for i in range(PERIOD):
        matrix[i][i] = 2
        matrix[i][(i + 1) % PERIOD] -= 2
        matrix[i][(i - 1) % PERIOD] -= 2
        matrix[i][(i + 3) % PERIOD] += 1 + delta[i]
        matrix[i][(i + 4) % PERIOD] += 1 + delta[(i + 4) % PERIOD]
    if any(matrix[i][j] != matrix[j][i]
           for i in range(PERIOD) for j in range(PERIOD)):
        raise ArithmeticError("The mixed-rank matrix is not symmetric.")
    return matrix


def zero_tuple_sanity() -> dict:
    """Verify the expected one-dimensional kernel of C at delta=0."""
    matrix = rank_matrix((0,) * PERIOD)
    row_sums = [sum(row) for row in matrix]
    cofactor = determinant_bareiss([row[:-1] for row in matrix[:-1]])
    determinant = determinant_bareiss(matrix)
    if row_sums != [0] * PERIOD or determinant != 0 or cofactor != 343:
        raise ArithmeticError("The standard-rank kernel check failed.")
    # Row sums zero give the constant kernel vector; the nonzero 6x6
    # principal minor proves that this kernel is exactly one-dimensional.
    return {
        "constant_vector_is_in_kernel": True,
        "determinant": determinant,
        "principal_6_by_6_minor": cofactor,
        "rank": 6,
    }


def compute_certificate() -> dict:
    sanity = zero_tuple_sanity()
    total_count = 0
    zero_mean_count = 0
    candidate_count = 0
    survivors = []
    nonzero_determinants = []
    candidate_digest = hashlib.sha256()
    for delta in product(DELTA_VALUES, repeat=PERIOD):
        total_count += 1
        if sum(delta) != 0:
            continue
        zero_mean_count += 1
        if any(delta[i] + delta[(i + 1) % PERIOD] > 1 for i in range(PERIOD)):
            continue
        candidate_count += 1
        determinant = determinant_bareiss(rank_matrix(delta))
        line = json.dumps([*delta, determinant], separators=(",", ":")) + "\n"
        candidate_digest.update(line.encode("utf-8"))
        if determinant == 0:
            survivors.append(list(delta))
        else:
            nonzero_determinants.append(determinant)

    if (total_count, zero_mean_count, candidate_count) != (78125, 8135, 890):
        raise ArithmeticError("The finite rank-candidate counts changed.")
    if survivors != [[0] * PERIOD] or len(nonzero_determinants) != 889:
        raise ArithmeticError("A nonstandard mixed-rank candidate survived.")

    return {
        "schema": "nc-p1123-mixed-ranks-v1",
        "date": "2026-11-19",
        "scope": (
            "Exact exhaustive elimination of necessary rank conditions; "
            "not a construction or AS-regularity test for relation data."
        ),
        "period": PERIOD,
        "delta_definition": "delta_i = r_3(i)-2",
        "delta_values": list(DELTA_VALUES),
        "necessary_conditions": [
            "sum_i delta_i = 0",
            "delta_i + delta_(i+1) <= 1 for every i modulo 7",
            "det(C) = 0",
        ],
        "matrix": {
            "shift_convention": "S_ij = 1 iff j=i+1 modulo 7; D=diag(delta)",
            "definition": "C=2I-2(S+S^-1)+S^3+S^4+D*S^3+S^4*D=P(1,1)",
            "size": [PERIOD, PERIOD],
            "symmetric": True,
        },
        "determinant_method": (
            "Fraction-free Bareiss elimination with row pivoting; "
            "every division checked exact; integer arithmetic only."
        ),
        "counts": {
            "all_range_tuples": total_count,
            "zero_mean_tuples": zero_mean_count,
            "zero_mean_and_adjacent_bound_tuples": candidate_count,
            "determinants_computed": candidate_count,
            "zero_determinants": len(survivors),
            "nonzero_determinants": len(nonzero_determinants),
        },
        "surviving_delta_tuples": survivors,
        "surviving_r3_tuple": [2] * PERIOD,
        "nonzero_determinant_statistics": {
            "minimum_absolute_value": min(abs(value) for value in nonzero_determinants),
            "maximum_absolute_value": max(abs(value) for value in nonzero_determinants),
            "negative_count": sum(value < 0 for value in nonzero_determinants),
            "positive_count": sum(value > 0 for value in nonzero_determinants),
        },
        "zero_tuple_sanity": sanity,
        "candidate_determinant_digest": {
            "algorithm": "SHA-256",
            "format": (
                "UTF-8 compact JSON lines [delta_0,...,delta_6,det(C)], "
                "lexicographic delta order, LF after each line."
            ),
            "value": candidate_digest.hexdigest(),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="recompute and write the current JSON certificate")
    args = parser.parse_args()
    certificate = compute_certificate()
    if args.write:
        CERTIFICATE_PATH.write_text(
            json.dumps(certificate, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {CERTIFICATE_PATH.name} from the exact computation.")
    else:
        if not CERTIFICATE_PATH.exists():
            raise SystemExit("Certificate missing; generate it with --write.")
        retained = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        if retained != certificate:
            raise SystemExit("Certificate mismatch: the exact recomputation differs.")
        print(f"Verified {CERTIFICATE_PATH.name} against the exact recomputation.")
    print("890 candidates checked; the only zero determinant is delta=(0,0,0,0,0,0,0).")
    print("These are necessary rank conditions, not an AS-regularity test.")


if __name__ == "__main__":
    main()
