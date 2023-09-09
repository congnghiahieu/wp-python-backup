from functools import partial

""" partial được sử dụng trong tình huống: ta có 1 hàm yêu cầu 2 tham số a,b. Trong đó ta có được rằng tham số a luôn cố định (bằng cách nào đó) và chỉ cần truyền tham số cho b """


def multiply(x: float, y: float):
    return x * y


multiply_by_6 = partial(multiply, 6)
multiply_by_7 = partial(multiply, 7)
multiply_by_8 = partial(multiply, 8)
multiply_by_9 = partial(multiply, 9)

print(multiply_by_6(5))
print(multiply_by_7(4))
print(multiply_by_8(3))
print(multiply_by_9(2))
