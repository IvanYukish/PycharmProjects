# ПЕРЕБІГ ПО ВСІМ КОМБІНАЦІЯМ ЕЛЕМЕНТІВ
from itertools import permutations
s,k = input().split()
for i in list(permutations(sorted(s), int(k))):
    print(*i,sep='')