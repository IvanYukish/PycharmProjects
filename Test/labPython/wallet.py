# гаманець
import random


def amount_of_debt(dictionary):
    print(sum(dictionary.values())*sum(dictionary.keys()))


lstA = (1, 2, 5, 10, 20, 50, 100, 200, 500)
dic = dict()
for i in range(10):
    rand = random.randint(0, 10)
    if rand:
        dic[random.choice(lstA)] = rand


print('Suma = ', end='')
amount_of_debt(dic)
