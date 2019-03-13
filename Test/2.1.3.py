a, b, c, d = (int(input()) for _ in range(4))
print("\t", ('\t'.join(str(x) for x in range(c, d + 1))))
for i in range(a, b + 1):
    print(i, end="")
    for j in range(c, d + 1):
        print("\t", i * j, end="")
    print()
