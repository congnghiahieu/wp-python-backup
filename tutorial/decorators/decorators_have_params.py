import time
from typing import Callable, Any
import functools
import logging

# NOTE: VD2: Decorator có tham số
# NOTE: Sẽ có 3 trường hợp có tham số: Decorator có tham số (logging), wrapper có tham số, func có tham số (greeting)
# NOTE: Decorator có thể được sử dụng cho nhiều hàm (Ví dụ: logger), nên ta không biết được sẽ truyền tham số như thế nào
# NOTE: Sử dụng *args, **kwargs để xử lý

# NOTE: Xử dụng Decorator functools.wraps(func) để đổi tên


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        value = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"Execute function {func.__name__} in {t2} second")

        return value

    return wrapper


def log(logger: logging.Logger):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Arguments: {args}")
            print(f"Keyword arguments: {kwargs}")

            print(f"Start Function {func.__name__}")
            value = func(*args, **kwargs)
            print(f"Value: {value}")
            print(f"End Function {func.__name__}")

            return value

        return wrapper

    return decorator


default_log = functools.partial(log, logger=logging.getLogger("my_logger"))


@log(logger=logging.getLogger("my_logger"))
@benchmark
def cal(*args: int) -> int:
    return sum(args)


cal(1, 2, 3, 4, 5)
