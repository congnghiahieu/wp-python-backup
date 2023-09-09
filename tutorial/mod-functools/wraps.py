from typing import Callable
from functools import wraps

""" wraps được sử dụng khi làm việc với decorator """

""" VD: Cách sử dụng decorator thông thường """


def greeting_oldway(func: Callable[..., int]):
    def wrapper_oldway(*args, **kwargs):
        print("Start oldway")
        print(func(*args, **kwargs))
        print("End oldway")

    return wrapper_oldway


@greeting_oldway
def add_oldway(x: int, y: int):
    """Add 2 number"""
    return x + y


add_oldway(2, 3)
print(f"Old way: {add_oldway.__name__}")  # wrapper
print(f"Old way: {add_oldway.__doc__}")  # None

"""
Ví dụ trên ta thấy rằng hàm add đã được hàm wrapper bọc nên __name__ và __doc__ là của hàm wrapper
Với trường hợp như ví dụ trên, ta muốn __name__ và __doc__ là của hàm add, ta sử dụng decorator wraps
"""


def greeting_newway(func: Callable[..., int]):
    @wraps(func)
    def wrapper_newway(*args, **kwargs):
        print("Start newway")
        print(func(*args, **kwargs))
        print("End newway")

    return wrapper_newway


@greeting_newway
def add_newway(x: int, y: int):
    """Add 2 number"""
    return x + y


add_newway(2, 3)
print(f"New way: {add_newway.__name__}")  # add
print(f"New way: {add_newway.__doc__}")  # Add 2 number
