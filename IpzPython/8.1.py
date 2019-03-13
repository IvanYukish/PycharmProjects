n, k = (int(input()) for _ in range(2))
lst = [1 for i in range(n)]
shot = count = 0
while lst.count(1) > 1:
    while count != k:
        if shot >= n:
            shot %= n
        if lst[shot] == 1:
            count += 1
            shot += 1
        else:
            shot += 1
    lst[shot - 1] = 0
    count = 0
print(lst.index(1) + 1)
