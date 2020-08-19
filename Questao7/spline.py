import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 22})  # font size
figsize = (19.2, 12)

def spline(pontos):
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
    return eq

fs = ["1 / (1 + x**2)",#1
    "1 / (1 + x**2)",#2
    "1 / ((1 + x**2)**(1/2))",#3
    "2 / (1 + x**2)", #4
    "2 / (1 + x**2)" #5
    ]

xss = [[-2, -1, 1, 2],
    [-2, -1, 0, 1, 2],
    [0, 0.3, 0.9, 1.3, 2],
    [-1.97, -1.16, -0.34, 0.32, 0.38, 0.61, 1.09, 1.44, 1.81, 1.82],
    [-4.65, -4.62, -4.39, -4.25, -4.01, -3.6, -3.52, -2.62, -0.75, 0.47, 0.77, 0.78, 1.44, 2.45, 2.91, 3.06, 3.17, 3.7, 4.49, 4.83],
]

for q in range(len(fs)):
    def f(x):
        return eval(fs[q])
    xs = xss[q]
    ys = [f(x) for x in xs]

    pontos = zip(xs, ys)
    
    print(f"### Questão {q+1}:")
    eqs = spline(pontos)

    plt.figure(figsize=figsize, constrained_layout=True)
    plt.title("Spline")
    for i in range(len(eqs)):
        def eq(x):
            return eval(eqs[i])

        a, b, inc = xs[i], xs[i + 1], 0.001
        t = np.arange(a, b + inc, inc)
        plt.plot(t, eq(t), label=f"eq{i}")

        print(f"eq{i}={eqs[i]}")
    print()    

    plt.scatter(xs, ys)
    plt.legend()
    # plt.show()
    plt.savefig(f"./plots/questao{q+1}.png", dpi=400)
