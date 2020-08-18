import numpy as np
import matplotlib.pyplot as plt

pontos = [(-2.5, -5.6), (-2.0, -4.03), (-1.5, -0.4), (-1.0, -1.12), (-0.5, 1.51), (0.0, 2.98), (0.5, -4.59), (1.0, 0.56), (1.5, -4.43),
(2.0, -5.53), (2.5, 2.14), (3.0, 4.02), (3.5, 0.85), (4.0, 1.37), (4.5, 5.26), (5.0, 2.79), (5.5, 5.16), (6.0, -2.28), (6.5, -2.9),
(7.0, -0.61), (7.5, -3.93), (8.0, 2.04), (8.5, 5.61), (9.0, -2.09), (9.5, 1.55), (10.0, -0.59), (10.5, -5.47), (11.0, -5.5),
(11.5, 2.64), (12.0, 2.0), (12.5, 5.1)]

def prod(lista):
    p = 1
    for i in lista:
        p *= i
    return p

def lagrange(pontos, x):
    # retorna o valor do polinômio de Lagrange que interpola
    # a lista 'pontos' calculado no ponto x
    xs, ys = zip(*pontos)
    soma = 0
    for k, y in enumerate(ys):
        xk = xs[k]
        Lk_numerador = prod([x - xi for i, xi in enumerate(xs) if i != k])
        Lk_denominador = prod([xk - xi for i, xi in enumerate(xs) if i != k])
        soma += y * (Lk_numerador / Lk_denominador)
    return soma

def p(x):
    return lagrange(pontos, x)


xs, ys = zip(*pontos)

# intervalo da função
a, b, step = min(xs), max(xs), 0.01
t = np.arange(a, b+step, step)

# função para interpolar
# def f(x):
#     return 1 / (1 + 25 * x ** 2)
# usado para desenhar o gráfico da função
# ft = [f(i) for i in t]
# plt.plot(t, ft, label="gráfico de f(x)")

# plotar os 'pontos'
plt.scatter(xs, ys)

# plotar o gráfico de p(x)
pt = [p(i) for i in t]
plt.plot(t, pt, label="polinômio interpolador", color="r")
plt.legend()
plt.title(f"Lagrange: {len(pontos)} pontos")
plt.show()

# Fenômeno de Runge

# plt.savefig(f"{len(pontos)} pontos", dpi=300)