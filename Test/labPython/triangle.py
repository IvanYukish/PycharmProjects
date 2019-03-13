import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return '({p1}, {p2}, {p3})'.format(p1=self.a, p2=self.b, p3=self.c)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def area(self):
        P = self.a + self.b + self.c
        S = math.sqrt(P * (P - self.a) * (P - self.b) * (P - self.c))
        return S

    def is_direct(self):
        return (self.a ** 2 == self.b ** 2 + self.c ** 2) or \
               (self.b ** 2 == self.a ** 2 + self.c ** 2) or \
               (self.c ** 2 == self.b ** 2 + self.a ** 2)

    def is_isotonic(self):
        return (self.a == self.b) or (self.b == self.c) or (self.a == self.c)


tr1 = Triangle(2, 3, 4)
tr2 = Triangle(4, 4, 5)
print(tr1 == tr2)
print(tr1.area())
print(tr1.is_direct())
print(tr1.is_isotonic())
print(tr2.is_isotonic())
print(tr1)
