# row_number = int(input())
# iterr = 0
# number = 1
# lst = []
# while iterr != row_number:
#     if number != lst.count(number):
#         lst.append(number)
#         iterr += 1
#     else:
#         number += 1
# print(*lst)


# a = int(input())
# b = []
# for i in range(1, a+1):
#     b += ([i] * i)
# print(*b[0:a])

print(*(lambda n: ("".join((str(x) + " ") * x for x in range(1, n + 1))).split()[:n])(int(input())))
