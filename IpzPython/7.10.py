def len_line():
    Stroka = input().split()
    print(Stroka)
    print(min([str(len(i)) for i in Stroka]))


len_line()