import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})  # font size
figsize = (19.2, 12)

def prod(lista):
    p = 1
    for i in lista:
        p *= i
    return p

def lagrange(pontos):
    # retorna o valor do polinômio de Lagrange que interpola
    xs, ys = zip(*pontos)

    global p, eq
    def p(x):
        # a lista 'pontos' calculado no ponto x
        soma = 0
        for k, y in enumerate(ys):
            xk = xs[k]
            Lk_numerador = prod([x - xi for i, xi in enumerate(xs) if i != k])
            Lk_denominador = prod([xk - xi for i, xi in enumerate(xs) if i != k])
            soma += y * (Lk_numerador / Lk_denominador)
        return soma

    def eq():
        eq = "p(x)="
        for k, y in enumerate(ys):
            xk = xs[k]
            Lk_numerador = "*".join([f"(x{-xi:+})" for i, xi in enumerate(xs) if i != k])
            Lk_denominador = "*".join([f"({xk}{-xi:+})" for i, xi in enumerate(xs) if i != k])
            eq += f"{y:+}*({Lk_numerador})/({Lk_denominador})"
        return eq

pnts = [
    [(-2.5,0.89),(-2.0,-1.18),(-1.5,1.88),(-1.0,4.06),(-0.5,1.21)],
    [(-2.5,-3.99),(-2.0,-5.26),(-1.5,0.54),(-1.0,-4.29),(-0.5,-2.59),(0.0,-0.95),(0.5,-0.15)],
    [(-2.5,0.94),(-2.0,-3.08),(-1.5,5.33),(-1.0,2.57),(-0.5,-5.94),(0.0,4.39),(0.5,-2.35),(1.0,0.17),(1.5,5.38),(2.0,-1.13),(2.5,-2.63)],
    [(-2.5,-5.6),(-2.0,-4.03),(-1.5,-0.4),(-1.0,-1.12),(-0.5,1.51),(0.0,2.98),(0.5,-4.59),(1.0,0.56),(1.5,-4.43),(2.0,-5.53),(2.5,2.14),(3.0,4.02),(3.5,0.85),(4.0,1.37),(4.5,5.26),(5.0,2.79),(5.5,5.16),(6.0,-2.28),(6.5,-2.9),(7.0,-0.61),(7.5,-3.93),(8.0,2.04),(8.5,5.61),(9.0,-2.09),(9.5,1.55),(10.0,-0.59),(10.5,-5.47),(11.0,-5.5),(11.5,2.64),(12.0,2.0),(12.5,5.1)]
    ]

for i in range(len(pnts)):
    print(f"### Questão {i+1}:")
    lagrange(pnts[i])

    xs, ys = zip(*pnts[i])
    a, b, step = min(xs), max(xs), 0.01
    t = np.arange(a, b + step, step)
    plt.figure(figsize=figsize, constrained_layout=True)
    plt.title("Lagrange")
    plt.scatter(xs, ys, label="Pontos", color="r")
    plt.plot(t, p(t), label="Polinômio Interpolador")
    # plt.show()
    plt.savefig(f"./plots/questao{i+1}.png", dpi=400)

    print("Polinômio:")
    print(eq())