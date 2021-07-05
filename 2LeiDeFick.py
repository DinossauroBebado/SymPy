
from sympy import *


# segunda lei de fick
def leiDeFick(variaveis, incognita):
    Cx, Czero, Cs, D, t, x = symbols("Cx, Czero,Cs,D,t,x")

    z = x/(2*sqrt(D*t))

    expr1 = (Cx-Czero)/(Cs-Czero)

    expr2 = 1 - erf(z)

    equa = Eq(expr1, expr2)

    res = solve(equa, incognita)[0].subs(variaveis)

    return(res)


def difusao(variaveis, incognita):

    Dzero, D, T, R, Q = symbols("Dzero,D, T, R, Q")

    expr1 = Dzero*exp(-Q/(R*T))
    expr2 = D

    equa = Eq(expr1, expr2)

    res = solve(equa, incognita)[0].subs(variaveis)

    return(res)


Cx, Czero, Cs, D, t, x = symbols("Cx, Czero,Cs,D,t,x")

Dzero, D, T, R, Q = symbols("Dzero,D, T, R, Q")

variaveis = [
    # (Cx, 0.3),
    (Czero, 0),
    (Cs, 0.2),
    (D, 1.9*10**-11),
    (t, 25*60*60),  # segundos
    (x, 2*10**-3)
]

variaveisDifusao = [
    (Dzero,  6.2*10**-7),
    #(D, 6.2*10**-7),
    (T, 600+273),  # kelvin
    (R, 8.31),
    (Q, 80*10**-3)]


print((difusao(variaveisDifusao, D).evalf()))

#print(N(leiDeFick(variaveis, Cx)))
