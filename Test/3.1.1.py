def func(x):
    return x <= -2 and (1 - (x + 2)**2) or -2 < x <= 2 and (-x / 2) or 2 < x and ((x - 2) ** 2 + 1)


print(func(float(input())))

