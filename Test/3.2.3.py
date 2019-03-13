def f(x):
    return x ** 2


a = [int(input()) for i in range(int(input()))]
b = {x: f(x) for x in set(a)}
print(*[b[i] for i in a])
print(b)
