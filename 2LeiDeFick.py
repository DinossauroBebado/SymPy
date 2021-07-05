
from sympy import *


# segunda lei de fick
def leiDeFick(variaveis, ingognita):
    Cx, Czero, Cs, D, t, x = symbols("Cx, Czero,Cs,D,t,x")

    z = x/(2*sqrt(D*t))

    expr1 = (Cx-Czero)/(Cs-Czero)

    expr2 = 1 - erf(z)

    equa = Eq(expr1, expr2)

    res = solve(equa, ingognita)[0].subs(variaveis)

    return(res)


Cx, Czero, Cs, D, t, x = symbols("Cx, Czero,Cs,D,t,x")

variaveis = [
    (Cx, 0.25),
    (Czero, 0.55),
    (Cs, 0),
    (D, 4.3*10**-11),
    (t, 36000)  # segundos
]

print(N(leiDeFick(variaveis, x)))
