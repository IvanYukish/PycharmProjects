def generatorOfInfinity(X):
    Y = list(X[3:]) + list(X[:3])
    Z = list(str(int(''.join(X)) * int(''.join(Y))))
    s = ''.join(Z[3:len(Z) - 3])
    yield s


result = generatorOfInfinity(input('Введіть початкове значення X - '))
print(result)
while True:
    inp = input("Продовжити? ")
    if inp == 'Y' or inp == 'y':
        for i in result:
            print(i)
            result = (i for i in result)
    else:
        break
