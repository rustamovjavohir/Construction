from typing import Type


class ValidPoint:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Point coordinate must be float or integer")
        instance.__dict__[self.name] = value


class Point3D:
    x = ValidPoint()
    y = ValidPoint()
    z = ValidPoint()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._a = 10


p1 = Point3D(1, 2, 3)

print(p1.__dict__)
print(p1._a)

if __name__ == '__main__':
    pass
