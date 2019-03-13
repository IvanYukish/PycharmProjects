import random


def amount_of_debt(dictionary):
    number_of_credits = 0
    number_of_exams = 0
    for i in dictionary.values():
        if i == "екзамен":
            number_of_credits += 1
        else:
            number_of_exams += 1
    print("кількість заліків = ", number_of_credits)
    print("кількість екзаменів = ", number_of_exams)


foo = ('екзамен', 'залік')
# словник створюється рандомно для економії часу
dic = {"Предмет" + str(i+1): random.choice(foo) for i in range(10)}
print(dic)
amount_of_debt(dic)
