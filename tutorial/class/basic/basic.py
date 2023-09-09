class Dog:
    """
    def __init__ là constructor - self ~ this
    - Nếu không định nghĩa tường minh def __init__ thì mặc định khởi tạo không cần tham số
    - Nếu có định nghĩa tường minh def __init__ thì phải khởi tạo theo tham số đã quy định ở __init__ constructor
    - Chỉ có thể sử dụng 1 def __init__. Nếu có định nghĩa nhiều hàm __init__ thì hàm init mới nhất (ở dưới cùng) sẽ được sử dụng (các hàm init ở trên sẽ bị bỏ qua)
    - Các method trong class bắt buộc phải có tham số đầu tiên là self
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print("Wolf!")


roger = Dog("Dave", 10, 1)
roger.request = "Hey Hey"  # Thêm thuộc tính ngoài được
print(roger.name)
print(roger.age)
print(roger.weight)
name = "Hieu cong nghia"
print(roger.__setattr__(name, "Cong"))  # set Attribute
print(roger.__getattribute__("request"))  # get Attribute
print(roger.__dict__)  # Class dưới dạng dict
roger.bark()


"""
Ví dụ 2
Có thể add và delete attribute của 1 instance
"""


class MyClass:
    """A simple example class"""

    def __init__(self, myint: int):
        self.i = myint

    def f(self):
        new = self.i**3
        return new


x = MyClass(4)
print(x.f())

# Thêm thuộc tính cho instance
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
# Xoá thuộc tính của instance
del x.counter
# print(x.counter) # Lỗi không thể lấy x.counter vì đã bị xoá
