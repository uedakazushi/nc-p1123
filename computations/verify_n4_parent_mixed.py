#!/usr/bin/env python3
"""Exact check of one failed AS6 mixed Euler extension of the pure model.
This rejects only the displayed mixed arrays; all possible extensions remain
unclassified.  Standard library only; no optimization solver is required.
"""
L = 10
D = (-1, 0, 0, 2, -1, 2, 0, 1, -1, 1)
A = (3, 4, 2, 4, 0, 2, 1, 3, 4, 2)
B = (2, 3, 3, 5, 3, 5, 3, 4, 3, 1)
R = tuple(d + 5 for d in D)
C = tuple(A[i] + A[(i + 1) % L] - 1 - B[(i + 5) % L] for i in range(L))
E = tuple(B[(i + 5) % L] + B[(i + 6) % L] - A[(i + 1) % L] - 1 for i in range(L))
assert min(C) >= 0 and min(E) >= 0
for i in range(L):
    bound = (A[i] - 1) * (A[(i + 1) % L] - 1) if A[i] and A[(i + 1) % L] else 0
    assert C[i] <= min(R[i], R[(i + 2) % L], bound)


def zero(): return [[0] * L for _ in range(L)]
def mv(M, x): return [sum(M[i][j] * x[j] for j in range(L)) for i in range(L)]
def dot(x, y): return sum(a * b for a, b in zip(x, y))
def trans(M): return [list(x) for x in zip(*M)]

K = zero()
Z = zero()
Kprime = zero()
for i in range(L):
    K[i][i] += 1
    K[i][(i + 1) % L] -= 2
    K[i][(i + 2) % L] += D[i]
    K[i][(i + 3) % L] += 1
    Kprime[i][(i + 1) % L] -= 2
    Kprime[i][(i + 2) % L] += 2 * D[i]
    Kprime[i][(i + 3) % L] += 3
    Z[i][(i + 2) % L] -= 1
    Z[i][(i + 3) % L] += A[i] - 2
    Z[i][(i + 4) % L] += B[(i + 5) % L] - 2
    Z[i][(i + 5) % L] -= 1
Z2 = [[Z[(j + 1) % L][(i - 1) % L] for j in range(L)] for i in range(L)]
r = (3, 1, 4, 3, 7, 2, 7, 4, 4, 1)
l = (13, 1, 12, 11, 21, 8, 26, 15, 22, 3)
y = (-19, 1, -34, -31, -75, -31, -69, -36, -28, 0)
assert mv(K, r) == [0] * L and mv(trans(K), l) == [0] * L
assert dot(l, mv(Kprime, r)) == -20
assert dot(l, mv(Z, r)) == 0
assert [a + b for a, b in zip(mv(K, y), mv(Z, r))] == [0] * L
second = dot(l, mv(Z2, r)) + dot(l, mv(Z, y))
assert second == -942
print('Exact mixed-extension check: PASS')
print('c =', C)
print('d =', E)
print('det(K0 + v Z + v^2 S^-1 Z^T S^-1 + v^3 S^-1 K0^T S^-1)')
print('  = -942 v^2 + O(v^3), although its constant and linear terms vanish.')
print('This mixed extension is excluded by the pure pole of order three.')
print('The pure model itself is NOT excluded for every possible mixed extension.')
