def http_error_1(status: int) -> str:
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case _:  # like default
            return "Unexpected error"


# Trong trường hợp muốn xử lý nhiều case cùng 1 kết quả
# Dùng | thay cho "or"
def http_error_2(status: int) -> str:
    match status:
        case 400 | 401 | 403 | 404:
            return "Client error"
        case 500 | 501 | 502 | 503:
            return "Server error"
        case _:
            return "Invalid error status code"


print(http_error_1(400))
print(http_error_2(101))

# Match có thể sử dụng để handle trường hợp 1 tuple cần unpack (hoặc có thể handle cả trường hợp unpack 1 list), và gán giá trị cho biến
# point tuple (x,y)

# List vẫn có thể unpack giống như tuple
(one, two, *three) = [1, 2, 3]
print(one)
print(two)
print(three)


def match_tuple(point: tuple | list) -> str | ValueError:
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):  # gán giá trị cho y
            return f"Y={y}"
        case (x, 0):  # gán giá trị cho x
            return f"X={x}"
        case (x, y):  # gán giá trị cho cả x và y
            return f"X={x} Y={y}"
        case _:  # default
            raise ValueError("Not a point")


print(match_tuple((0, 0)))
print(match_tuple((0, 100)))
print(match_tuple((10, 0)))
print(match_tuple((123, 21321)))
print(
    match_tuple([1, 2])
)  # Vì list này chỉ có 2 phần tử tương đương 1 tuple (x,y) nên có thể coi là vẫn unpack được "list". Nếu list này có 1 hoặc 3 phần tử thì sẽ lỗi
# print(match_tuple([1,2,3])) => Lỗi

# Advanced
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def where_is(point: Point) -> None:
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):  # gán giá trị cho y
            print(f"Y={y}")
        case Point(x=x, y=0):  # gán giá trị cho x
            print(f"X={x}")
        case Point(x=x, y=y):  # gán giá trị cho cả x và y
            print(f"X={x} Y={y}")
        case _:  # default
            print("Not a point")


where_is(Point(0, 0))
where_is(Point(0, 10))
where_is(Point(10, 0))
where_is(Point(10, 10))
