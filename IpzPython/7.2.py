def palindron():
    Stroka = input().lower().strip().replace(' ', '')
    print(Stroka)
    print(Stroka[::-1])
    if Stroka == Stroka[::-1]:
        return True
    else:
        return False


print(palindron())