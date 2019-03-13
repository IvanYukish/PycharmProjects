lst = list((map(int, input().split())))
count = int(input())
lst2 = [i for i, e in enumerate(lst) if e == count]
if count not in lst:
    print("Отсутствует")
else:
    print(*lst2)
