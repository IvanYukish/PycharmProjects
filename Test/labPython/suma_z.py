import random

def amount_of_debt(dictionary):
    print(sum(dictionary.values()))


dic = {"Послуга" + str(i): random.randint(2000, 3000) for i in range(10)}
print(dic)
print('Suma = ', end='')
amount_of_debt(dic)
