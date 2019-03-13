import math


def f(a, b):
    y = ((a - 6) / (2 * a + b)) + (math.sin(3 * a) / math.cos(b))
    return y


print(f(0.03, 0.04))
