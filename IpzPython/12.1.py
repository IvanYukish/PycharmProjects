import math


class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def distance(self, B):
        return math.sqrt((self.X - B.X) ** 2 + (B.Y - self.Y) ** 2)

    def __eq__(self, B):
        return self.X == B.X and self.Y == B.Y

    def __str__(self):
        return '({X}, {Y})'.format(X=self.X, Y=self.Y)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        if not self.is_existence:
            raise Exception("triangle does not exist")

    @property
    def is_existence(self):
        """
        check if Triangle exists
        if one point does not lie on another
        if the length of one of the sides does not exceed the bag of the rest
        """
        if self.p1 == self.p2 or self.p1 == self.p3 or self.p2 == self.p3:
            return False

        if (self.p3.X * (self.p2.Y - self.p1.Y) -
                self.p3.Y * (self.p2.X - self.p1.X)
                == self.p1.X * self.p2.Y - self.p2.X * self.p1.Y):
            return False
        else:
            return True

    @property
    def perimeter(self):
        return (self.p1.distance(self.p2) + self.p1.distance(self.p3)
                + self.p2.distance(self.p3)) / 2

    @property
    def area(self):
        return math.sqrt(
            self.perimeter * (self.perimeter - (self.p1.distance(self.p2))) *
            (self.perimeter - (self.p1.distance(self.p3))) *
            (self.perimeter - (self.p2.distance(self.p3))))

    def __str__(self):
        return '({p1}, {p2}, {p3})'.format(p1=self.p1, p2=self.p2, p3=self.p3)


if __name__ == '__main__':
    myPoint1 = Point(1, 0)
    myPoint2 = Point(300, 3)
    myPoint3 = Point(0, 3)

    print(myPoint1, myPoint2, myPoint3)
    print(myPoint3 == myPoint2)
    myTriangle = Triangle(myPoint1, myPoint2, myPoint3)
    print(myTriangle)
    print(myTriangle.perimeter)
    print(myTriangle.area)
