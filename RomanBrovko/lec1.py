def add(a, b):
    return a + b


def bar():
    return add('5', '6')


lst = (1, 2, 3, 4, 5)
sets = {i for i in range(10)}
print(sets, type(sets))

Dict = {'el-' + str(i): i * 2 for i in range(1, 5)}
# print(Dict)
# print(*Dict.items())
# print(*Dict.keys())
# print(type(Dict.values()))
Dict['a'] = 3
# print(Dict)
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
Dict['b'] = users
# print(Dict)
Dict[lst] = 'b'
print(Dict)
i=0
while i<4:
   i+=1
   if i == 3:
     print('555')
     break
else:
    print('s')
s = set(range(10))
print(s)
s = {"w" for i in range(10)}
print(s)




