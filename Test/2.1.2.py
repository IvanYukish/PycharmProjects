A,B = (int(input())for _ in range(2))
if(A>B):
    NOD1 = A
    while NOD1 % B != 0:
        NOD1 += A;
    print(NOD1)
else:
    NOD1 = B
    while NOD1 % A != 0:
        NOD1 += B;
    print(NOD1)

