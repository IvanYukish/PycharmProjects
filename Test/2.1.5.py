A, B = (int(input() )for _ in range(2))
it = sums = 0
for _ in range(A, B+1):
    if _%3 == 0:
        sums += _
        it += 1
print(sums/it)