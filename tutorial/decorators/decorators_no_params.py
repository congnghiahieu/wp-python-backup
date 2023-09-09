import time
from typing import Callable, Any

# NOTE: Decorator là 1 trong 23 desgin pattern
# NOTE: Decorator có 2 kiểu là class (design pattern truyền thống, Java) và function (TS, Python)
# NOTE: Decorator truyền thống sẽ có dạng: decorator(func)()
# NOTE: Trong Python (hoặc TS, JAVA), @decorator ~ hàm func sau khi đánh @decorator sẽ biến thành decorator(func) (=== wrapper)
# NOTE: Hàm func sau khi được đánh @, nếu gọi hàm func() ~ decorator(func)() ~ wrapper()


# NOTE: VD1: Decorator không có tham số
# Hàm count_time là 1 decorator
# Hàm count_time_type là 1 hàm bọc của decorator (count_time_type chỉ bọc chứ không phải 1 decorator khác)
# 1 decorator nhận vào 1 hàm (func) và trả về 1 hàm (gọi là wrapper)
# wrapper có thể gọi hàm func(), có thể thực hiện gì đó trước hoặc sau khi gọi hàm func
# NOTE: Cú pháp @count_time sẽ bọc hàm do_something_1 => count_time(do_something_1)
# Khi gọi hàm do_something_1() ~ count_time(do_something_1)()


def count_time_type(type: str):
    print("Count_time_type")

    def count_time(func: Callable[[], Any]):  # Đây là decorator
        def wrapper():
            print(f"{type}")
            t1 = time.time()
            func()
            t2 = time.time() - t1
            print(f"{func.__name__} executed in {t2} second")
            print(f"{type}")

        return wrapper

    print("Count_time_type")

    return count_time


@count_time_type("Type 3")
@count_time_type("Type 1")
def do_something_1():
    time.sleep(1)


@count_time_type("Type 4")
@count_time_type("Type 2")
def do_something_2():
    time.sleep(2)


do_something_1()  # ~ count_time(count_time(do_something_1))()
do_something_2()  # ~ count_time(count_time(do_something_2))()
