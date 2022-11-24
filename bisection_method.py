from math import *


def bisection_method(func, a, b, error_accept):

    def f(x):
        f = eval(func)
        return f

    if f(a) * f(b) >= 0:
        raise ValueError("No hay raíces presentes, el método de bisección no funcionará.")

    i = 0
    error = abs(b - a)

    while error > error_accept:
        c = (a + b) / 2

        if f(c) < 0:
            a = c
            error = abs(b - a)
            i += 1

        elif f(c) > 0:
            b = c
            error = abs(b - a)
            i += 1

        else:
            raise ValueError("Error en la ejecución.")

    print(f"Iteraciones: {i}")
    print(f"Error: {error}")
    print(f"Límite inferior: {a}")
    print(f"Límite superior: {b}")


bisection_method("x * log(x) + e ** (-x) - 2", 2, 3, 0.05)