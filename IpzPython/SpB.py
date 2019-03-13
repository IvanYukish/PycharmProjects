from datetime import datetime
import math


def dec(funk):
    def wrapper():
        start = datetime.now()
        result = funk()
        print(datetime.now() - start)
        return result

    return wrapper()


@dec
def company():
    for i in range(int(input())):
        a, b, c = (int(i) for i in input().split())
        numbers = c * (max(a, b))
        for num in range(1, numbers):
            if (num % a) == 0 or (num % b) == 0:
                c -= 1
            if c == 0:
                print(num)
                break


@dec
def companyB():
    for i in range(int(input())):
        x, y, n = map(int, input().split())
        a = min((math.ceil((max((x, y)) / float(x + y)) * n) * min((x, y)),
                 math.ceil((min((x, y)) / float(x + y)) * n) * max((x, y))))
        print(a, end=' ')


# a = company()
# b = companyB()
# print(type(companyB))