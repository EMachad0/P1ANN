from math import *

# uma função qualquer
def f(x):
    return cos(sin(x**2)) + x**3 - 2

n = 50
# a raiz precisa estar dentro do intervalo
a, b = [1, 2]

for i in range(n):
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a))

    if f(xn) == 0:
        print('A raiz é:', xn)
    elif f(a) * f(xn) < 0: # teorema de Bolzano
        b = xn
    else:
        a = xn


print(xn, f(xn))