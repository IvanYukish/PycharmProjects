import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Точка має такі координати  X = {}, Y = {}'.format(self.x, self.y)

    def is_axis(self):
        if self.x == 0 or self.y == 0:
            return True
        else:
            return False

    def distance_points(self, other):
        if isinstance(other, Point):
            return math.sqrt(math.pow((other.x - self.x), 2) + (math.pow(other.y - self.y, 2)))
        else:
            return "Error"

    def middle_point(self, other):
        if isinstance(other, Point):
            return Point((self.x + other.x) / 2, (self.y + other.y) / 2)
        else:
            return "Error"

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.y == other.y and self.x == other.x:
                return True
            else:
                return False
        else:
            return 'NOT isinstance'


p1 = Point(2, 3)
p2 = Point(10, 10)

print(p1)
print(p1.is_axis())
print(p1.distance_points(p2))
print(p1.middle_point(p2))
print(p1 == p2)
