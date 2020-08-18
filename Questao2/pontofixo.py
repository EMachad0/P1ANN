from math import *

def ponto_fixo(funcao, x0, intervalo, n=10):
    # seja g:[a,b] -> R
    # 0. g tem que ser contínua
    # 1. g(x) pertence [a,b] para todo x pertence [a,b] é o mesmo que g([a, b])\subset[a,b]
    # 2. |g'(x)| < 1 para todo x pertence [a,b]
    # f(x) = 0 <-> g(x) = x

    global g
    def g(x):
        return eval(funcao)

    a, b = intervalo
    itr = [x0]
    for i in range(1, n+1):
        x0 = g(x0)
        itr.append(x0)
    
    return itr


fs = ["x**2 - 7", #1
    "x**3 - 11", #2
    "x**3 - 11", #3
    "x**3 - 11", #4
    "e**x - 2*x - 1", #5
    "x**3 - x - 4", #6
    "x**4 - x**2 - 5", #7
    "sin(x) - 2*x + 4"] #8

gs = ["1/2*(x+7/x)", #1
    "1/2*(x+11/x**2)", #2
    "(11/x)**(1/2)", #3
    "x-(x**3-11)/(3*x**2)", #4
    "log(2*x+1)", #5
    "(x+4)**(1/3)", #6
    "(x**2+5)**(1/4)", #7
    "(sin(x)+4)/2"] #8

intervalos = [(2, 3), (2, 3), (2, 2.5), (2, 3), (1, 2), (1, 2), (1, 2), (2, 3)]

for i in range(len(fs)): #questoes
    def f(x):
        return eval(fs[i])

    print(f"### Questao {i+1}:")
    x0 = (intervalos[i][1] - intervalos[i][0])/2 
    itr = ponto_fixo(gs[i], x0, intervalos[i])
    print(f"Aproximação da raiz de f pelo método do ponto fixo no intervalo {intervalos[i]} com x0 = {x0} é")
    print("|itr | x | g(x) | f(x)|")
    print("|----|---|------|-----|")
    for j, x in enumerate(itr):
        print(f"|{j} | {x} | {g(x)} | {f(x)}|")
    print()