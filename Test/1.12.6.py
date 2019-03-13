X = int(input());
if 5 <= (X % 10) <= 9 or 11 <= (X % 100) <= 19 or X % 10 == 0:
    print(X, " программистов")
elif 2 <= (X % 10) <= 4:
    print(X, "программиста")
else:
    print(X, "программист")
