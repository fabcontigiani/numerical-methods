from math import *


def simpsons38_rule(func, lower_limit, upper_limit):

    def f(x):
        return eval(func)

    h = (upper_limit - lower_limit) / 3

    integral = (upper_limit - lower_limit) * ((f(lower_limit) + 3*f(h) + 3*f(2*h) + f(upper_limit))/8)

    print(f"Resultado: {integral}")


simpsons38_rule("(sin(1+sqrt(x)))/(1+x**2)", 0, 2)
