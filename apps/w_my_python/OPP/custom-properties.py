class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    old = property(get_age, set_age)


p = Person('Ali', 20)
# p.set_age(30)
p.old = 30
print(p.get_age(), p.__dict__)

if __name__ == '__main__':
    pass
