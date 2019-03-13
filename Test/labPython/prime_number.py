import math

# перевірка на просте число
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True


def num(number):
    for i in range(number, 2, -1):
        if isPrime(i):
            print(i)
            break
    for i in range(number + 1, int(math.pow(number, 2))):
        if isPrime(i):
            print(i)
            break


num(int(input('Введіть число - ')))
