from math import *


def simpsons13_rule(func, lower_limit, upper_limit):

    def f(x):
        return eval(func)

    h = (upper_limit - lower_limit) / 2

    integral = (upper_limit - lower_limit) * ((f(lower_limit) + 4*f(h) + f(upper_limit))/6)

    print(f"Resultado: {integral}")


simpsons13_rule("(sin(1+sqrt(x)))/(1+x**2)", 0, 2)
