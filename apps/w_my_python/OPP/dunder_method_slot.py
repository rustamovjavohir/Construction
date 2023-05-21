class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    """ __slot__ sinf misollarida xotiradan foydalanish va
    atributlarga kirishni optimallashtirish uchun ishlatiladi.
    bunda xotiradan foydalanishni optimallashtirgai uchun __dict__ atributi ishlatilmaydi.
    """
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fun1(self):
        pass


class Point3D(Point2D):
    __slots__ = ('z',)
    MAX_1 = 100

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def hello(self):
        return 'Hello'


p = Point(10, 20)
p2d = Point2D(10, 20)
p3d = Point3D(10, 20, 30)

print(Point3D.__dict__)

# print(p.__dict__)
if __name__ == '__main__':
    pass
