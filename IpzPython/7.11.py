text = str(input("Enter text: "))
l = text.split()
q = ""


def f(a):
    return len(a)


for i in sorted(l, key=f):
    q = q + " " + i
print(q)
