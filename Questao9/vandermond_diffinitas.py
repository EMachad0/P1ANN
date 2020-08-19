from math import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})  # font size
figsize = (19.2, 12)

def vandermond(pontos):
    xs, ys = zip(*pontos)
    n = len(xs)

    A = [[x ** k for k in range(n)] for x in xs]
    B = ys
    vand = np.linalg.solve(A, B)

    global p, eq
    def p(x):
        px = sum([vand[k] * x ** k for k in range(n)])
        return px

    def eq():
        eq = "p(x)="
        eq += "".join([f'{vand[k]:+}*x**{k}' for k in range(n)])
        return eq

def f1(x0, h): # f1
    return (p(x0 + h) - p(x0 - h)) / (2*h)

def f2(x0, h): # f2 com erro h**2
    return (p(x0 + h) - 2 * p(x0) + p(x0 - h)) / h**2

def f3(x0, h): # f3
    return ((-1/2)*p(x0+(-2*h)) + p(x0+(-1*h)) - p(x0+(1*h)) + (1/2)*p(x0+(2*h))) / (h**3)

fs = ["x**x", "cos(x)", "e**x"]

xss= [[0.99, 1, 1.01],
    [0.99, 1, 1.01, 1.02],
    [0.98, 0.99, 1, 1.01]]

for q in range(len(fs)):
    def f(x):
        return eval(fs[q])
    
    xs = xss[q]
    ys = [f(x) for x in xs]

    print(f"### Questão {q+1}:")
    pontos = zip(xs, ys)
    vandermond(pontos)

    a, b, step = min(xs), max(xs), 0.001
    t = np.arange(a, b + step, step)
    plt.figure(figsize=figsize, constrained_layout=True)
    plt.title("vandermond")
    plt.scatter(xs, ys, label="Pontos", color="r")
    plt.plot(t, p(t), label="Polinômio Interpolador")
    # plt.show()
    plt.savefig(f"./plots/questao{q+1}.png", dpi=400)

    print("Polinômio:")
    print(eq())

    print("|h|F_1(1)|F_2(1)|F_3(1)|")
    print("|--|--|--|--|")
    for i in range(1, 11):
        h = 1/2**i
        print(f"|{h}|{f1(1, h)}|{f2(1, h)}|{f3(1, h)}|")
    print()
