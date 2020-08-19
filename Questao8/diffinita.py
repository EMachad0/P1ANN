from math import *

fs = ["cos(x**x)",
    "sin(x)",
    "x**(cos(x))",
    "e**(-x**2)"]

dfs = ["(f(p)-f(p-h))/h",
    "(f(p+h)-f(p-h))/(2*h)",
    "(f(p-2*h)-8*f(p-h)+8*f(p+h)-f(p+2*h))/(12*h)"]

hs = [0.1, 0.05, 0.025, 0.0125]

p = 1
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
            r.append(df(p, h))
        print("", h, *r, "", sep="|")
    print()