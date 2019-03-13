import random
dic = {"P" + str(i) : [random.randint(50, 100) for j in range(10)] for i in range(5)}
print(dic)
a = 0
for i in dic:
    print(sum(dic[i])/len(dic[i]))


print(max([sum(dic[i])/len(dic[i]) for i in dic]))
