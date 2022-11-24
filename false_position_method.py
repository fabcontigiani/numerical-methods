from math import *


def false_position_method(func, a, b, error_accept):

    def f(x):
        return eval(func)

    if f(a) * f(b) >= 0:
        raise ValueError("No existen raíces o múltiples raíces presentes. Método no será útil.")

    i = 0
    c = b - ((f(b) * (a-b))/(f(a) - f(b)))
    error = abs(c - 0)

    while error > error_accept:

        c = b - ((f(b) * (a-b))/(f(a) - f(b)))

        if f(c) < 0:
            error = abs(c - a)
            a = c
            i += 1

        elif f(c) > 0:
            error = abs(c - b)
            b = c
            i += 1

        else:
            raise ValueError("Error en la ejecución.")

    print(f"Iteraciones: {i}")
    print(f"Error: {error}")
    print(f"Raíz aproximadamente en {c}")
    print(f"Límite inferior: {a}")
    print(f"Límite superior: {b}")


false_position_method("x * log(x) + e ** (-x) - 2", 2, 3, 0.01)
