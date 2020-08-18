from math import *

def secante(funcao, x0, x1, n = 10):
    # uma função qualquer
    global f
    def f(x):
        return eval(funcao)

    # a raiz NAO precisa estar dentro do intervalo
    a, b = x0, x1

    itr = [x0, x1]
    for i in range(2, n+1):
        try:
            # a - f(a) / ((f(b) - f(a))/ (b - a))
            xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) 
        except:
            print(f"Divisão por zero na iteração {i}")
            break

        itr.append(xn)
        if f(xn) == 0:
            break
        a, b = b, xn

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

for i in range(len(funcoes)): #questoes
    print(f"### Questao {i+1}:")
    itr = secante(funcoes[i], 0.1, 0.5)
    print(f"Aproximação da raiz de f pelo métodos das secantes é")
    print("|itr | xn | f(xn)|")
    print("|----|----|------|")
    for i, xn in enumerate(itr):
        print(f"|{i} | {xn} | {f(xn)}|")
    print()