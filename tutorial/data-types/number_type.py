import math

# integer type
price = 80
best_price = int(100)
print(type(price))
print(isinstance(price, int))

# float type
gpa = 3.98
score = float(3.98)

# complex type: Số phức gồm phần thực và phần ảo
# phần ảo kí hiệu là j
complex_num = 2 + 5j
complex_num2 = complex(3 + 6j)
print(type(complex_num))
print(complex_num.real)
print(complex_num.imag)

# built-in math function
print(abs(gpa * -1))  # Lấy giá trị tuyệt đối
print(round(gpa))  # Làm tròn giữ phần nguyên
print(round(gpa, 1))  # Làm tròn đến số thập phân thứ 1

# math module
print(math.pi)
print(math.e)
print(math.sqrt(gpa))
print(math.ceil(gpa))
print(math.floor(gpa))

# Cast a string to number
num_in_str = "1000"
print(type(int(num_in_str)))

# Lỗi khi cast sai giá trị
