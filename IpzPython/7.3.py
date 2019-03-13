def brackets():
    Stroka = ''.join(input().split())
    lstB = ['(', ')', '<', '>', '{', '}', '[', ']']
    Stroka = ''.join([i for i in Stroka if i in lstB])
    translation_set = ['()', '[]', '{}', '<>']
    while any(i in Stroka for i in translation_set):
        for i in translation_set:
            if i in Stroka:
                Stroka = Stroka.replace(i, '')

    return not bool(Stroka)


print(brackets())
