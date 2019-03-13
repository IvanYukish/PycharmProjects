print(type(1/2)) #+

names = ['Amir']
if 'amir' in names:#+
    print(1)
else:
    print(2)

print(4.5//2) #+

print(chr(104)+chr(105)) #+

Dic = {} #+
Dic[1] = 1
Dic['1'] = 2
Dic[1.0] = 4
sum = 0
for i in Dic:
    sum+= Dic[i]
print(sum)

# Tup = (1,2)  # -
# Tup.append((5,6,7))
# print(len(Tup))

def myFunk(x,y,z,a): #+
    print(x+y)
lst=[1,2,3,4]
myFunk(*lst)

class Person: #-
    def __init__(self,id):
        self.id = id
obama = Person(100)
obama.__dict__['age'] = 49
print(obama.age + len(obama.__dict__))
print(obama.__dict__)

