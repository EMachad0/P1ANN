from sympy import *
from math import *

def newton(funcao, x0):
    x = symbols("x")
    derivada = str(diff(funcao, "x", 1))
    # print(derivada)

    # uma função qualquer
    def f(x):
        return eval(funcao)

    # derivada de f
    def df(x):
        return eval(derivada)

    # ponto inicial
    n = 10 # numero de iterações

    itr = [x0]
    for i in range(1, n+1):
        x0 = x0 - f(x0) / df(x0)
        itr.append(x0)
        if f(x0) == 0:
            break

    print(f"Aproximação da raiz de f é")
    print("|itr | xi | f(xi)|")
    print("|----|----|------|")
    for i in range(len(itr)):
        print(f"|{i} | {itr[i]} | {f(itr[i])}|")

funcoes = ["x**5 - 8*x - 2", #1
    "cos(x**2) - x", #2
    "log(x) + x**2", #3
    "log(x**2) + 2*x", #4
    "cos(sin(x**2)) + x**3 - 2", #5 
    "e**(-x**2) - x**2 + 5", #6
    "e**(cos(x)) + log(x**2)", #7
    "x**2 * cos(x) + x -1", #8
    "2*cos(e**x)-x", #9
    "x**3 + x**2 + 0.001"] #10

for i in range(10): #questoes
    print(f"### Questao {i+1}:")
    newton(funcoes[i], 1)
    print()