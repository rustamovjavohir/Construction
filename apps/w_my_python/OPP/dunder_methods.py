class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # __str__ is called by print() and str()
    def __str__(self):
        return f'a {self.color} car'

    # __repr__ is called by repr()
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color}, {self.mileage})'

    def __getattribute__(self, item):
        # print(f'__getattribute__({item})')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # print(f'__setattr__({key}, {value})')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print(f'__getattr__({item})')
        return super().__getattribute__(item)

    def __delattr__(self, item):
        print(f'__delattr__({item})')
        return super().__delattr__(item)


my_car = Car('red', 37281)
# print(my_car)
# print(str(my_car))
# my_car.salom = 'salom'
# print(my_car.alik)
# print(repr(my_car))
# my_car.__getattribute__('mileage')
print(my_car.__dict__)
my_car.__delattr__('mileage')
print(my_car.__dict__)
if __name__ == '__main__':
    pass
