from math import *

def bissection(funcao, intervalo, n = 10):
    # função
    global f
    def f(x):
        return eval(funcao)

    # método da bisseção
    l, r = intervalo
    itr = [0]

    for i in range(n):
        m = (l + r) / 2
        if f(m) == 0:
            print('A raiz é:', m)
        elif f(l) * f(m) < 0: # teorema de Bolzano
            r = m
        else:
            l = m
        itr.append(m)

    return itr

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

intervalos = [(-5, 5), (-5, 5), (0.1, 5), (0.1, 5), (-5, 5), (-5, 5), (0.1, 5), (-5, 5), (-5, 5), (-5, 5)]

for i in range(len(funcoes)): #questoes
    print(f"### Questao {i+1}:")
    itr = bissection(funcoes[i], intervalos[i])
    print(f"Aproximação da raiz de f no intervalo {intervalos[i]} é")
    print("|itr | m | f(m)|")
    print("|----|---|-----|")
    for i in range(1, len(itr)):
        print(f"|{i} | {itr[i]} | {f(itr[i])}|")
    print()