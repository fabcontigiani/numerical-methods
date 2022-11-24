from math import *


def newtons_method(func, func_derivative, x, error_accept, max_iter=10):

    def f(x):
        return eval(func)

    def df(x):
        return eval(func_derivative)

    i = 0
    error = inf

    while error > error_accept and i <= max_iter:
        next_x = x - (f(x)/df(x))
        error = abs(next_x - x)
        x = next_x
        i += 1

    if i > max_iter:
        print("Límite de iteraciones alcanzado. Posible resultado divergente.")

    print(f"Raíz encontrada: {x} luego de {i} iteraciones.")


newtons_method("cos(sqrt(x)) - ((sin(x))/2)", "-((sin(sqrt(x)))/(2 * sqrt(x))) - (cos(x))/2", 0.25, 0.05)
