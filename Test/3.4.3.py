with open('dataset_3363_4.txt', 'r') as file:
    lstA = []
    for Stroka in file:
        lstA.append([i.strip() for i in ''.join(Stroka).split(";")])
lstA[::] = [int(i) if i.isdigit() else i for outer in lstA for i in outer]
lstA[::] = zip(*[iter(lstA)] * 4)
[print((matan+fizra+rus)/3) for name, matan, fizra, rus in lstA]
print(sum([matan for name, matan, fizra, rus in lstA])/len(lstA), sum([fizra for name, matan, fizra, rus in lstA])/len(lstA),sum([rus for name, matan, fizra, rus in lstA])/len(lstA))

# st = [x.split(';') for x in open('dataset_3363_4.txt').readlines()]
# print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
# print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1, 4)])
