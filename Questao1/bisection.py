from math import *

def bissection(funcao, intervalo): # intervalo
    # função
    def f(x):
        return eval(funcao)

    # método da bisseção
    l, r = intervalo
    n = 10 # número de iterações

    for i in range(n):
        m = (l + r) / 2
        if f(m) == 0:
            print('A raiz é:', m)
        elif f(l) * f(m) < 0: # teorema de Bolzano
            r = m
        else:
            l = m

    print(f"Aproximação de {funcao} é {m} tq")
    print(f"f({m}) = {f(m)}")

funcoes = ["x**5 - 8*x - 2", #1
    "cos(x**2) - x", #2
    "log(x) + x**2", #3
    "log(x**2) + 2*x", #4
    "cos(sin(x**2)) + x**3 - 2", #5 
    "pow(e, -x**2) - x**2 + 5", #6
    "pow(e, cos(x)) + log(x**2)", #7
    "x**2 * cos(x) + x -1", #8
    "2*cos(e**x)-x", #9
    "x**3 + x**2 + 0.001"] #10

intervalos = [(-5, 5), (-5, 5), (0.1, 5), (0.1, 5), (-5, 5), (-5, 5), (0.1, 5), (-5, 5), (-5, 5), (-5, 5)]

for i in range(10): #questoes
    print(f"Questao {i+1}:")
    bissection(funcoes[i], intervalos[i])
    print()