Stroka = input().lower().split()
Dictionary = dict()
for i in set(Stroka):
    Dictionary[i] = Stroka.count(i)
for key in Dictionary:
    print(key,Dictionary[key])