def func(strok):
    i = 0
    number = 0
    lis = ['a', 'e', 'i', 'o', 'u', 'y']
    for strok in lis:
        number += int(strok.count(lis[i]))
        i += 1
    print(number)


func("afterburner")
