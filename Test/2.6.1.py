sp = [int(input())]
while sum(sp)!=0:
    sp.append(int(input()))
print(sum(el ** 2 for el in sp))
