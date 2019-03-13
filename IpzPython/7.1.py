#зсув слова
def cut (k):
    Stroka = input()
    if k < 0:
        for i in range(-k):
            Stroka = Stroka[1::]+Stroka[0]
        return Stroka
    for i in range(k):
        Stroka = Stroka[len(Stroka)-1]+Stroka[:len(Stroka)-1:]

    return Stroka

print(cut(-2))
print(cut(2))