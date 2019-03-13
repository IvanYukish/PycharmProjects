import math
import operator


def axis_rotation():
    number, alfa = input().split()
    Dictionary = {}
    for i in range(int(number)):
        name, X, Y = input().split()
        newX = float(X) * math.cos(int(alfa)) + int(Y) * math.sin(int(alfa))
        newY = float(X) * math.sin(int(alfa)) + int(Y) * math.cos(int(alfa))
        Dictionary[name] = (int(newY), int(newX))

    return Dictionary


Sort = (sorted(axis_rotation().items(), key=operator.itemgetter(1)))
print(Sort)
for i in Sort:
    print(i[0])
