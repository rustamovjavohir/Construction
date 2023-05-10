class ThreadData:
    __shared_state = {
        "name": "thread_1",
        "data": {},
        "id": 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return str(self.__shared_state)


th1 = ThreadData()
th2 = ThreadData()

th2.name = 'thread_2'
th2.id = 2

print(th2.__dict__)
print(th1.__dict__)

if __name__ == '__main__':
    pass
