from sympy import *

print(sqrt(18))

frac = Rational(25, 15)

print(frac)

x, y = symbols("x,y")

expr = 3*x + y

print(expr)
print(solve(expr, y))
