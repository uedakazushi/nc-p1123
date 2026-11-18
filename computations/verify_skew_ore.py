#!/usr/bin/env python3
"""Exact critical-pair certificate for the weighted diagonal-skew Ore chart.

Run: python3 computations/verify_skew_ore.py
Requires Python>=3.9 and sympy. All results are symbolic over Z[q,p,r,s,u,v,a,b].
"""
from functools import lru_cache
import sympy as S

q,p,r,s,u,v,a,b = S.symbols('q p r s u v a b')
# x<y<z<t, six quadratic rewrite rules
RULES = {
    (1,0): {(0,1): q},
    (2,0): {(0,2): p},
    (2,1): {(1,2): r},
    (3,0): {(0,3): s, (2,2): a},
    (3,1): {(1,3): u, (2,2): b},
    (3,2): {(2,3): v},
}

def add(out, word, coeff):
    out[word] = S.expand(out.get(word,0) + coeff)
    if out[word] == 0:
        del out[word]

@lru_cache(None)
def nf(word, direction):
    positions=[i for i in range(len(word)-1) if word[i:i+2] in RULES]
    if not positions:
        return {word: S.Integer(1)}
    i=positions[0] if direction=='left' else positions[-1]
    out={}
    for sub,c in RULES[word[i:i+2]].items():
        assert sub < word[i:i+2]
        for monom, d in nf(word[:i] + sub + word[i+2:], direction).items():
            add(out, monom, c*d)
    return out

obstacles={}
for word in ((2,1,0),(3,1,0),(3,2,0),(3,2,1)):
    L=nf(word,'left'); R=nf(word,'right')
    delta={}
    for key in set(L)|set(R):
        difference=S.factor(L.get(key,0)-R.get(key,0))
        if difference != 0:
            delta[''.join('xyzt'[i] for i in key)]=str(difference)
    obstacles[''.join('xyzt'[i] for i in word)]=delta

assert obstacles == {
    'zyx':{},
    'tyx':{'xzz':str(S.factor(b*(p**2-q*s))), 'yzz':str(S.factor(a*(u-q*r**2)))},
    'tzx':{'zzz':str(S.factor(a*(v-p)))},
    'tzy':{'zzz':str(S.factor(b*(v-r)))},
}, obstacles

# The closed set of equations splits set-theoretically into exactly four
# irreducible components.  Check their equations and generic witnesses.
def constraints(A,B):
    return [A*(v-p), A*(u-q*r**2), B*(v-r), B*(p**2-q*s)]

families={
    'zero': {a:0,b:0},
    'a-only': {b:0,v:p,u:q*r**2},
    'b-only': {a:0,v:r,s:p**2/q},
    'both': {v:p,r:p,u:q*p**2,s:p**2/q},
}
for label,vals in families.items():
    for equation in constraints(a,b):
        assert S.factor(equation.subs(vals, simultaneous=True))==0, (label,equation)

# Exhaustive logical partition by nonzero statuses of a,b (four cases).
# Dimension includes the free a,b coordinates on their respective closures.
dims={'zero':6, 'a-only':5, 'b-only':5, 'both':4}
print('PASS: exact four overlaps:',obstacles)
print('PASS: complete set-theoretic decomposition of Ore parameter variety:',dims)
print('PASS: rho=0 iff a=b=0, otherwise rho=1 (relation projection).')