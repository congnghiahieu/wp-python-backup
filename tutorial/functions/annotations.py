# Annotations - Chú thích
# Thêm chú thích kiểu cho biến, hoặc kiểu trả về của 1 hàm
# Annotations chỉ có tác dụng thêm thông tin khi dev. Không có tác dụng static type checking (Nếu sử dụng tool khác như "mypy" thì có thể có chức năng static type checking), không có tác dụng khi runtime


def increment(n: int) -> int:
    """Increment a number by one"""
    return n + 1


count: int = 1


# 1 biến (hoặc trả về) có thể là nhiều kiểu
# Dùng | để thêm annotations có nhiều kiểu
# Thêm annotation và gán giá trị default
def match_tuple(point: tuple | list, option: dict = {}) -> str | ValueError:
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
