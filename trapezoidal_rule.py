from math import *


def trapezoidal_rule(func, lower_limit, upper_limit, n):

    def f(x):
        return eval(func)

    step_size = (upper_limit - lower_limit) / n

    integral = f(lower_limit) + f(upper_limit)

    for i in range(1, n):
        integral += 2 * f(lower_limit + i*step_size)

    integral = (upper_limit - lower_limit) * (integral / (2*n))

    print(f"Resultado: {integral}")


trapezoidal_rule("(sin(1+sqrt(x)))/(1+x**2)", 0, 2, 3)
