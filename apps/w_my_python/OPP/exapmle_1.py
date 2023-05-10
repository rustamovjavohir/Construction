from string import ascii_letters
import re


class Person:
    letters = ascii_letters + "'`"
    passport_re = "[A-Z]{2}[0-9]{7}$"

    def __init__(self, fio, old, ps, weight):
        self.varify_fio(fio)
        self.varify_old(old)
        self.varify_passport(ps)

        self.__fio = fio
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def varify_fio(cls, fio):
        if len(fio.split()) < 3:
            raise ValueError('FIO must be equal or more than 3 words. Example: "Ivanov Ivan Ivanovich"')
        if not all([True if i in cls.letters else False for i in fio.replace(' ', '')]):
            raise ValueError('FIO must be only letters')

    @classmethod
    def varify_old(cls, old):
        if not isinstance(old, int):
            raise ValueError('Old must be integer')
        if not 18 < old < 60:
            raise ValueError('Old must be between 18 and 60')

    @classmethod
    def varify_passport(cls, ps):
        if not isinstance(ps, str):
            raise ValueError('Passport must be string')
        if not re.match(cls.passport_re, ps.upper()):
            raise ValueError('Passport must be like AA1234567')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.varify_fio(value)
        self.__fio = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.varify_old(value)
        self.__old = value

    def get_passport(self):
        return self.__passport

    def set_passport(self, value):
        self.varify_passport(value)
        self.__passport = value

    property(get_passport, set_passport)


person = Person('Rustamov Javohir Xolmuhammad o\'g\'li', 23, 'AA1234567', 70)
print(person.__dict__)
person.fio = 'Karimov Alisher Saidovich'
print(person.__dict__)
if __name__ == '__main__':
    pass
