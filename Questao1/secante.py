from math import *

# uma função qualquer
def f(x):
    return cos(sin(x**2)) + x**3 - 2

n = 50
# a raiz NAO precisa estar dentro do intervalo
x0, x1 = [1, 2]

itr = [x0, x1]

a, b = x0, x1
for i in range(2, n):
    try:
        # a - f(a) / ((f(b) - f(a))/ (b - a))
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) 
    except:
        print("Divisão por zero para {:.2f}, {:.2f} na iteração {:d}".format(a, b, i))
        break
    itr.append(xn)
    a, b = b, xn

print(b, f(b))