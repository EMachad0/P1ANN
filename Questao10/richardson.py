from math import *

def fk(x, h, n, p):
    # I'm recursive :)
    if n == 1:
        return df(x, h)
    n -= 1
    return (2 ** (n * p) * fk(x, h/2, n, p) - fk(x, h, n, p)) / (2 ** (n * p) - 1)

fs = ["cos(x**x)",
    "sin(x)",
    "x**(cos(x))",
    "e**(-x**2)"]

dfs = ["(f(p)-f(p-h))/h",
    "(f(p+h)-f(p-h))/(2*h)",
    "(f(p-2*h)-8*f(p-h)+8*f(p+h)-f(p+2*h))/(12*h)"]

hs = [0.1, 0.05, 0.025, 0.0125]

ns = [4, 2, 1] # ordem do erro
x0 = 1 # ponto
p = 1 # b ???????????

for q in range(len(fs)):
    def f(x):
        return eval(fs[q])
    
    print(f"### Questão {q+1}:")
    print("|h|erro O(h)|erro O(h^2)|erro O(h^4)|")
    print("|--|--|--|--|")
    for h in hs:
        r = []
        for i in range(len(dfs)):
            def df(p, h):
                return eval(dfs[i])
            r.append(fk(x0, h, ns[i], p))
        print("", h, *r, "", sep="|")
    print()

# import sympy as sy
# x = sy.Symbol('x')
# f = sy.sympify('x ** x')
# df = sy.diff(f, x, 2).subs(x, x0).evalf()
# print('exact:', df)