from accessify import protected, private


class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate_coord(cls, coord):
        return cls.MIN_COORD <= coord <= cls.MAX_COORD

    def __new__(cls, *args, **kwargs):
        # print('new')
        return super().__new__(cls)

    def __init__(self, x, y, z, t):
        # print('init')
        if not (self.validate_coord(x) and self.validate_coord(y)):
            raise ValueError('Координаты должны быть в диапазоне от {} до {}'.format(self.MIN_COORD, self.MAX_COORD))
        self.x = x
        self.y = y
        self._z = z
        self.__t = t

    def get_coord(self):
        return self.x, self.y, self._z, self.__t

    @private
    def get_t(self):
        return self.__t

    @protected
    def get_z(self):
        return self._z


pt = Point(1, 2, 3, 4)
pt2 = Point(4, 5, 6, 7)
pt._z = 100
# print(pt.x, pt.y, pt._z, pt.__t)
# print(pt.get_coord())
# print(pt.get_z())

if __name__ == '__main__':
    pass
