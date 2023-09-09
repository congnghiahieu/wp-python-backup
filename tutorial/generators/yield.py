""" Ý tưởng của Generator là chỉ lưu 1 giá trị vào 1 thời điểm """


class Generator:
    def __init__(self, n: int) -> None:
        self.n = n
        self.last = 0

    def __next__(self):
        return self._next()

    def _next(self):
        if self.last == self.n:
            raise StopIteration()
        res = self.last**2
        self.last += 1
        return res


class_gen = Generator(100)
print("Self Implement")
while True:
    try:
        print(next(class_gen))
    except StopIteration:
        break

"""
yield keyword

Có 2 cách để sử dụng yield keyword:
- Vòng lặp while, next và try / except StopIteration
- Sử dụng vòng lặp for
"""


def generator_yield(n: int):
    for i in range(n):
        yield i**2


yield_while_gen = generator_yield(100)
yield_for_gen = generator_yield(100)
print("Yield While loop, next and try / except")
while True:
    try:
        print(next(yield_while_gen))
    except StopIteration:
        break

print("Yield For loop")
for num in yield_for_gen:
    print(num)

""" Nhiều yield ở trong 1 hàm """


def multi_yield():
    x = 1
    y = 2
    yield x
    yield y

    for i in range(3, 100):
        yield i**3


multi_yield_gen = multi_yield()
print(next(multi_yield_gen))  # 1 (x)
print(next(multi_yield_gen))  # 2 (y)
print(next(multi_yield_gen))  # 27 (3 ** 3)
print(next(multi_yield_gen))  # 64 (4 ** 3)
print(next(multi_yield_gen))  # 125 (5 ** 3)
