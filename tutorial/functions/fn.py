# Function
# Use keyword "def"
# Đặt tên cho func: sử dụng "_" và lowwer case
# 1 funcion có thể return hoặc không


def hello_world():
    print("Hello World")


hello_world()


def sum(num1, num2):
    print(num1 + num2)


sum(100, 200)


def mul(a, b):
    return a * b


print(mul(2, 10))


# Ngoài sử dụng == và !=, ta có thể sử dụng "is" và "is not" cho điều kiện if else
# Có thể kết hợp sử dụng "is", "is not", "in", "not in"
def sum_adv(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2


print(sum_adv("A", 100))
print(sum_adv(200, 100))
print(1 is not 2)  # print(1 != 2)


# Sử dụng default parameter
def mul_adv(num1=1, num2=1):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 * num2


print(mul_adv())
print(mul_adv(4, 5))
print(mul_adv("Hieu", 5))


# Hàm chấp nhận unknown number of args, dùng * (giống toán tử ... "rest")
# Tất cả các tham số nhận vào sẽ được đưa vào 1 tuple
# Ta hoàn toàn có thể cast kiểu tuple thành list để thuận tiện cho biến đổi
# Nếu chỉ cần loop qua thì có thể dùng for in tuple
def mul_arg(*args):
    print(args)
    print(type(args))  # <class 'tuple'>
    for unknown in args:
        print(unknown)


mul_arg(
    "Hieu", "Cong", "Nghia", 1, 10, 9, 2
)  # args = ('Hieu', 'Cong', 'Nghia', 1, 10, 9, 2)

# Hàm chấp nhận unknown number of keyword args (kwargs)
# Tất cả các keyword arg sẽ được đưa vào 1 dict, với tên biến là key và giá trị của biến là value
# Có thể For in để duyệt qua dict.keys() hoặc dict.values()


def mul_keyword_args(**kwargs):
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>


mul_keyword_args(name="Hieu", first="Cong", last="Nghia", one=1, ten=10, nine=9, two=2)
# dict = {'name': 'Hieu', 'first': 'Cong', 'last': 'Nghia', 'one': 1, 'ten': 10, 'nine': 9, 'two': 2}
