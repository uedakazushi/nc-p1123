#!/usr/bin/env python3
"""Exact checks of the displayed n=3 and n=4 numerical identities.

These are supplementary checks of polynomial/matrix identities in the paper
and notes. They neither construct an algebra nor establish AS regularity,
positivity of every Hilbert coefficient, or the analytic growth arguments.
All parameters are symbolic; no floating point or parameter sampling is used.
Run with the SymPy dependency in requirements-symbolic.txt.
"""

import sympy as sp


def cyclic_shift(size):
    return sp.Matrix(size, size, lambda i, j: int(j == (i + 1) % size))


def zero_matrix(matrix):
    assert all(sp.expand(entry) == 0 for entry in matrix)


u, v, a = sp.symbols("u v a")

# note:n3-direct-mixed-ranks: full scalar Euler polynomial.
p3 = (
    1 - u * (3 + v + v**2)
    + u**2 * (3 + a * v + a * v**2 + v**3)
    - u**3 * (1 + a * v + a * v**2 + 3 * v**3)
    + u**4 * (v + v**2 + 3 * v**3) - u**5 * v**3
)
expected3 = (
    (1 - u)**3 * (1 - u * v) * (1 - u * v**2)
    + (a - 3) * u**2 * (1 - u) * (v + v**2)
)
assert sp.expand(p3 - expected3) == 0

# genidx:lem:three-light-base-numerics: construct the full seven-row
# Euler matrix directly from ranks and shifts, then take its determinant.
s7 = cyclic_shift(7)
q7 = sp.diag(1, 0, 0, 0, 0, 0, 0)
r7 = 2 * sp.eye(7) + q7
p7 = sp.eye(7) - 3 * u * s7 + u**2 * r7 * s7**2 - u**9 * q7 * s7**9
assert sp.expand(p7.det(method="domain-ge") - (1 - u**7)**2 * (1 - 64 * u**7)) == 0

# n4:thm:top-word-divisible-three: the s=5 two-vertex Euler matrix.
alpha = sp.symbols("alpha")
beta = -1 - alpha
s2 = cyclic_shift(2)
i2 = sp.eye(2)
r2 = sp.diag(alpha + 5, beta + 5)
t2 = sp.diag(alpha + 3, beta + 3)
f2 = i2 - u * s2
k2 = i2 - 2 * u * s2 + u**2 * sp.diag(alpha, beta) + u**3 * s2
p2 = i2 - 4 * u * s2 + u**2 * r2 - u**4 * t2 + u**5 * s2
zero_matrix(p2 - f2 * k2 * f2)
assert sp.expand(k2.det() - (1 - 5 * u**2 + (alpha * beta + 4) * u**4 - u**6)) == 0

# The s=6 scalar denominator is negative at the displayed rational point.
assert (1 - 4 * u + 4 * u**2 - 2 * u**5 + u**6).subs(u, sp.Rational(1, 2)) == -sp.Rational(3, 64)

# n4:lem:periodic-pd3-obstruction: local identities in the analytic proof.
ell, delta, c, m = sp.symbols("ell delta c m")
assert sp.expand(
    -ell * (ell - 1) / 2 - delta**2 / 2 - ell * delta
    - ell / 2 + (ell + delta)**2 / 2
) == 0
assert sp.expand(
    (2 * c**2 - 1) - m * c + (m - 1) - (1 - c) * (m - 2 - 2 * c)
) == 0

print("PASS: n3 scalar Euler factorization and full seven-row determinant")
print("PASS: n4 s5 matrix factorization/determinant and s6 value -3/64")
print("PASS: Fourier factorization and second-variation square completion")
