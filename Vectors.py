from logging import warning
import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)

    def __mul__(self, other):

        if type(other) == Vector2D:
            return self.x*other.x+self.y*other.y

        if type(other) in [int, float]:
            return Vector2D(self.x*other, self.y*other)
    
    def __truediv__(self, other):

        if type(other) == Vector2D:
            raise NameError("not made yet")

        if type(other) in [int, float]:
            return Vector2D(self.x/other, self.y/other)

    def __str__(self) -> str:
        return "({0},{1})".format(self.x, self.y)

    def __pow__(self, other):

        if type(other) == int:
            if other == 1:
                return self

            return self*(self**(other-1))

        else:
            raise NameError("not made yet")

    def __eq__(self, other, ignore_warnings=False) -> bool:
        if type(other) == Vector2D:
            return self.x == other.x and self.y == other.y
        else:
            warning("You have compered a {0} with a {1}. default output is False".format(
                type(other), type(self)))
            return False

    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2)
