#!/usr/bin/env python3
"""Exact certificate for a formal n=4, s=5 pure Euler datum.

This constructs NO algebra and NO AS parent.  It proves that the displayed
Euler data have polynomial, nonnegative formal Hilbert coefficients satisfying
the dimension inequalities from a domain in every degree.  The finite checks
below imply all-degree assertions by the rational-degree argument in the
accompanying Japanese TeX note.  Standard library only.
"""

L = 10
PERIOD = 40
EXCESS_SECOND_DIFFERENCE = 38016
D = (-1, 0, 0, 2, -1, 2, 0, 1, -1, 1)
R = tuple(d + 5 for d in D)
P3 = tuple(R[i] + R[(i + 1) % L] - 9 for i in range(L))
P4 = tuple(7 - R[(i + 1) % L] for i in range(L))
Q = (1,) * L


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def trace(a):
    return sum(a[i][i] for i in range(3))


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


# Nonnegative Betti ranks, row/column balance, first moment, and the domain
# upper bound on quadratic relations.
assert min(R) >= 0 and max(R) <= 9
assert min(P3) >= 0 and min(P4) >= 0
for i in range(L):
    assert R[i] == 3 + P3[i] + P4[i] - Q[i]
    assert R[i] == 3 + P3[(i - 1) % L] + P4[(i - 2) % L] - Q[(i - 3) % L]
assert sum(P3) + 2 * sum(P4) - 3 * sum(Q) == 2 * L

# For K = I - 2uS + u^2 diag(D) S^2 + u^3 S^3, its scalar recurrence is
# g_(i+3) = -g_i + 2g_(i+1) - D_i g_(i+2).
M = [[int(i == j) for j in range(3)] for i in range(3)]
for d in D:
    T = [[0, 1, 0], [0, 0, 1], [-1, 2, -d]]
    M = matmul(T, M)
assert M == [[22, -47, -4], [6, -13, -1], [41, -87, -8]]
second = sum(M[i][i] * M[j][j] - M[i][j] * M[j][i]
             for i in range(3) for j in range(i + 1, 3))
assert (trace(M), second, det3(M)) == (1, 1, 1)
# char_M(x) = x^3 - x^2 + x - 1 = (x-1)(x^2+1).
# Consequently det K(u) = (1-u^10)(1+u^20), and
# det P(u) = (1-u^10)^3(1+u^20), where P=(I-uS) K (I-uS).

# P H = I determines the actual formal row coefficients exactly.
H = [[1] for _ in range(L)]
for n in range(1, 3 * PERIOD):
    for i in range(L):
        h = 4 * H[(i + 1) % L][n - 1]
        if n >= 2:
            h -= R[i] * H[(i + 2) % L][n - 2]
        if n >= 3:
            h += P3[i] * H[(i + 3) % L][n - 3]
        if n >= 4:
            h += P4[i] * H[(i + 4) % L][n - 4]
        if n >= 5:
            h -= H[(i + 5) % L][n - 5]
        H[i].append(h)

C = [[H[i][a] for a in range(PERIOD)] for i in range(L)]
B = [[H[i][a + PERIOD] - H[i][a] for a in range(PERIOD)] for i in range(L)]
A = [[H[i][a + 2 * PERIOD] - 2 * H[i][a + PERIOD] + H[i][a]
      for a in range(PERIOD)] for i in range(L)]
assert all(x == EXCESS_SECOND_DIFFERENCE for row in A for x in row)
assert min(x for row in C for x in row) == 1
assert min(x for row in B for x in row) == 22620
# The cofactor degree bound gives (1-u^40)^3 H_i(u) of degree <=115<120.
# Thus, for EVERY m>=0 and 0<=a<40, not merely for checked degrees:
# h_i(40m+a) = 38016*binom(m,2) + B[i][a]*m + C[i][a].

# Certify the Hopf inequality h_i(j+k)>=h_i(j)+h_(i+j)(k)-1 for all j,k>=0.
# Write j=40x+a, k=40y+b.  The difference is A*x*y + U*x + V*y + W,
# with the following finitely many exact integer coefficients.
minima = [10**100] * 3
for i in range(L):
    for a in range(PERIOD):
        for b in range(PERIOD):
            carry, residue = divmod(a + b, PERIOD)
            U = EXCESS_SECOND_DIFFERENCE * carry + B[i][residue] - B[i][a]
            V = EXCESS_SECOND_DIFFERENCE * carry + B[i][residue] - B[(i + a) % L][b]
            W = carry * B[i][residue] + C[i][residue] - C[i][a] - C[(i + a) % L][b] + 1
            assert U >= 0 and V >= 0 and W >= 0
            minima = [min(old, value) for old, value in zip(minima, (U, V, W))]

assert H[0][2] == 12 and H[1][2] == 11
print("Exact formal Euler certificate: PASS")
print("R =", R)
print("P3 =", P3)
print("P4 =", P4)
print("det P = (1-u^10)^3(1+u^20)")
print("All h_i(40m+a) = 38016*binom(m,2) + B_i,a*m + C_i,a")
print("min B = 22620; min C = 1; min(U,V,W) =", tuple(minima))
print("All-degree positivity, polynomial growth, and Hopf dimension inequalities hold.")
print("Hilbert rows differ: h_0(2)=12, h_1(2)=11.")
print("No algebra realization or AS6 parent realization is asserted.")
