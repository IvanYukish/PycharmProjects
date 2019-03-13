import math

a = float(input('a='))
b = float(input('b='))
if b > 0 and a >= 0:
    x = (math.sqrt(a * b))/math.pow(math.e, a)*b+a*math.pow(math.e, 2*a/b)
    print(x)
else:
    print("Not valid")
