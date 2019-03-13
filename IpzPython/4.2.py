import math

x, y, z = map(float, input().split())


def f(x, y, z):
    return (1.0 / (z * math.sqrt(2 * math.pi))) * math.e**(-((math.pow((x - y), 2.0)) / 2.0 * math.pow(z, 2)))


print(f(x, y, z))