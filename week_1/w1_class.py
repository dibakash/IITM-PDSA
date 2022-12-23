import math

"""
learning objectives:
overriding built ins: prints __str__, __add__ etc
"""


class Point:
    def __init__(self, a=0, b=0):
        self._x = a
        self._y = b
        self._r = math.sqrt(a * a + b * b)
        if a == 0:
            self._theta = math.pi / 2
        else:
            self._theta = math.atan(b / a)

    @property
    def odistance(self):
        return self._r

    @odistance.setter
    def odistance(self, d):
        self._r = d

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, deg):
        rad = math.radians(deg)
        if self._theta != rad:
            self._theta = rad
            self.x = self.odistance * math.cos(rad)
            self.y = self.odistance * math.sin(rad)

    def translate(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_x
        self.odistance = math.sqrt(self.x**2 + self.y**2)
        if self.x == 0:
            self.theta = math.pi / 2
        else:
            self.theta = math.atan(self.y / self.x)

    def __str__(self):
        print(f"coordinate is ({self.x:.1f},{self.y:.1f})")
        print(f"distance from the origin is {self.odistance:.3f} units")
        print(f"angle is {math.degrees(self.theta):.2f} deg", end="")
        return ""

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)


print(math.radians(90))

a = Point(3, 4)
print(a)

b = a + Point(10, 10)
print(b)
