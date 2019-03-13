def encryption():
    Stroka = ''.join([chr(ord(i) + 1) for i in input()])
    return Stroka

print(encryption())