A, B, C = (int(input()) for _ in range(3))
print(max(A, B, C), "\n", min(A, B, C), "\n", (A + B + C) - (max(A, B, C) + min(A, B, C)))
