from sympy.solvers import solve
from sympy import Symbol
T = Symbol('T')

year = solve([(472.85*(1.08**(T-1995)) +(-198.12))-(2439)], T)
print(year)