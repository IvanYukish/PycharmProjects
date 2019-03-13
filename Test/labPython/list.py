# список чисел
import random
lstA = [random.randint(-50, 50) for i in range(1,11)]
lstB = list()

for i in lstA:
    if i > 0:
        lstB.append(i)
for i in lstA:
    if i < 0:
        lstB.append(i)

print(lstA)
print(lstB)
