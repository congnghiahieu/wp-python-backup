# More: https://www.youtube.com/watch?v=Lv1treHIckI&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP&index=6

"""
with keyword là 1 hình thức của context manager

VD:
with open("text.txt", "w") as file:
    file.write("Hello")

Với ví dụ trên thì "as file" được gọi là __enter__
file.write("Hello") được gọi là center
Khi kết thúc phần center sẽ đến __exit__

"""

# with open("text.txt", "w") as file:
#     file.write("Hello")


class File:
    """
    Có thể tự tạo 1 context manager bằng class sử dụng 2 dunder method là __enter__ và __exit__

    __enter__ trả về gì thì "as file" nhận kiểu đó

    __exit__ được gọi trong trường hợp:
    - Center code thực hiện bình thường không có lỗi
    - Center xuất hiện Exception thì __exit__ vẫn được thực hiện. Nhưng thêm vào đó sẽ có 3 tham số được truyền tham vào hàm __exit__: 1 - exception_type (trả về Exception Class), 2 - exception_value (trả về message của Exception), 3 - traceback object

    Với __exit__, ta có thể trả về True (nếu lỗi đã được xử lý) thì chương trình sẽ không bị crash. Nếu trả về False hoặc không trả về (trả về None) thì chương trình sẽ bị crash

    VD:
    def __exit__(self, exception_type, exception_msg, traceback):
        print("Exit context manager")
        print(f"Type: {exception_type}")
        print(f"Value: {exception_msg}")
        print(f"Traceback: {traceback}")
        self.file.close()

        if type == SomeKnownException:
            return True

    """

    def __init__(self, filepath: str, open_mode: str) -> None:
        self.file = open(file=filepath, mode=open_mode)

    def __enter__(self):
        print("Enter context manager")
        return self.file

    def __exit__(self, exception_type, exception_msg, traceback):
        print("Exit context manager")
        print(f"Type: {exception_type}")
        print(f"Value: {exception_msg}")
        print(f"Traceback: {traceback}")
        self.file.close()

        if exception_type is Exception:
            return True


with File("context-manager/text.txt", "w") as f:
    print("Center context manager")
    f.write("Hello World")

    raise Exception("This is a handled exception")
    # raise FileExistsError("This is a unhandled exception")
