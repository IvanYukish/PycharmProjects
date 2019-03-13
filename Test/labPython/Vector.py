class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, b):
        return self.y == b.x and self.y == b.y

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)


class Vector:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '({p1}, {p2})'.format(p1=self.p1, p2=self.p2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(
                (self.p1.x + other.p2.x),
                (self.p1.y + other.p2.y),
            )
        else:
            raise Exception("Not type")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(
                (self.p1.x - other.p2.x),
                (self.p1.y - other.p2.y),
            )
        else:
            raise Exception("Not type")

    def __len__(self):
        return self.mag()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.p1.x * other,
                self.p1.y * other
            )
        elif isinstance(other, Vector):
            return Vector(
                self.p1.x * other.p2.x,
                self.p1.y * other.p2.y)

    def mag(self):
        return int((self.p1.x ** 2 + self.p1.y ** 2) ** 0.5)


if __name__ == '__main__':
    myPoint1 = Point(1, 4)
    myPoint2 = Point(300, 3)

    myPoint3 = Point(10, 45)
    myPoint4 = Point(30, 8)

    print(myPoint1, myPoint2)
    print(myPoint1 == myPoint2)

    Vector1 = Vector(myPoint1, myPoint2)
    Vector2 = Vector(myPoint3, myPoint4)

    Vector1.__str__()
    print(Vector2)

    print(Vector1 + Vector2)
    print(Vector2 - Vector2)

    print(Vector1 * Vector2)
    print(Vector2 * 4)

    print(len(Vector1))
    print(len(Vector2))
