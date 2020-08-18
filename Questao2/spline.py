import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1 / (1 + x**2)

xs = [-2, -1, 1, 2]
pontos = [(x, f(x)) for x in xs]

xs, ys = zip(*pontos)
n = len(xs) - 1
h = [xs[k+1] - xs[k] for k in range(n)]

# Matrix (N+1) por (N+1) ou len(pontos) por len(pontos)
matrix = []
first_row = [1] + [0 for _ in range(n)]
matrix.append(first_row)
for i in range(1, n):
    zeros_before = [0 for _ in range(i - 1)]
    zeros_after = [0 for _ in range(i + 1, n)]
    row = zeros_before + [h[i - 1], 2 * (h[i - 1] + h[i]), h[i]] + zeros_after
    matrix.append(row)
last_row = [0 for _ in range(n)] + [1]
matrix.append(last_row)

B = [0] + [3 * (ys[k+1] - ys[k]) / h[k] - 3 * (ys[k] - ys[k-1]) / h[k-1] for k in range(1, n)] + [0]

solucao = np.linalg.solve(matrix, B)

c = [v for v in solucao]
b = [(ys[k+1] - ys[k]) / h[k] - h[k] * (2 * c[k] + c[k+1]) / 3 for k in range(n)]
d = [(c[k+1] - c[k]) / (3 * h[k]) for k in range(n)]

eq = [f'{ys[k]}{b[k]:+.2f}*(x{-xs[k]:+}){c[k]:+.2f}*(x{-xs[k]:+})**2{d[k]:+.2f}*(x{-xs[k]:+})**3' for k in range(n)]
for i in range(n):
    print(f"eq {i}:", eq[i])

for i in range(n):
    def s(x):
        return eval(eq[i])

    a, b, inc = xs[i], xs[i + 1], 0.01
    t = np.arange(a, b + inc, inc)
    plt.plot(t, s(t))

plt.scatter(xs, ys)
plt.show()