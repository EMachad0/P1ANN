import sympy as sp
from math import *


f = input("Funcao:")
df = dp.diff(f, 1)

# uma função qualquer
def f(x):
    return eval(f)

# derivada de f
def df(x):
    return eval(df)

x0 = 2 # ponto inicial
n = 10 # numero de iterações

itr = [x0]
for i in range(1, n):
    x0 = x0 - f(x0) / df(x0)
    itr.append(x0)

print(x0, f(x0))
