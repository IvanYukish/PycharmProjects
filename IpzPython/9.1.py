Dictionary = {str(i): i for i in range(2, 11)}
Dictionary['J'] = 10
Dictionary['Q'] = 10
Dictionary['K'] = 10
Dictionary['T'] = 11

print("Вкажіть які карти хочете витягнути: ")
Karta = input().split()
lst = [Dictionary[i] for i in Karta if i in Dictionary]
if sum(lst) < 21:
    print(sum(lst))
elif (Dictionary['T'] in lst) and sum(lst) < 31:
    lst[lst.index(Dictionary['T'])] = 1
    print(sum(lst))
else:
    print("Bust")
