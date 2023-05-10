class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

    def __len__(self):
        return self.count


class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise ValueError('Seconds must be integer')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60  # seconds
        m = (self.seconds // 60) % 60  # minutes
        h = (self.seconds // 3600) % 24  # hours
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, cls)):
            raise ValueError(f'Other must be integer or {cls} class')
        return other.seconds if isinstance(other, cls) else other

    def __add__(self, other):
        sc = self.__verify_data(other)
        return self.__class__(self.seconds + sc)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        sc = self.__verify_data(other)
        self.seconds += sc
        return self

    def __sub__(self, other):
        sc = self.__verify_data(other)
        return self.__class__(self.seconds - sc)

    def __isub__(self, other):
        sc = self.__verify_data(other)
        return self.seconds - sc

    def __rsub__(self, other):
        return self.__sub__(other)

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


# c = Counter()
# c()
# c()
# print(len(c))

# c1 = Clock(800)
# c2 = Clock(1800)
# c3 = Clock(1800)
#
# c4 = 1000 - c1
# c3 += 1000
# print(c4.get_time())


fr = FRange(1, 10, 2)

if __name__ == '__main__':
    pass
