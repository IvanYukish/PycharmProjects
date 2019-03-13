# from collections import Counter
#
# with open('dataset_3363_3 (4).txt', 'r') as inf:
#     file = inf.read().lower().strip().split()
# c = Counter(w for w in file)
# print(*list(*c.most_common(1)))

# lstB = {i: Stroka.count(i) for i in set(Stroka)}
# print(lstB)

with open('dataset_3363_3 (4).txt','r') as file:
    s = file.read().strip().lower().split()

z = {i: s.count(i) for i in s}

maximum = max(z, key=z.get)
x = {maximum: z[maximum]}
print(x)