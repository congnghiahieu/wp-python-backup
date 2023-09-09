# Gán giá trị như bình thường
first = "Cong"
last = "Hieu"

# Để kiểm tra độ dài sử dụng len(string)
print(len(first + last))

# string index và string range index
s = "Công Nghĩa Hiếu"
print(s[0])
# s[1:]: Lấy từ index số 1 đến hết chuỗi. Không chỉ định kí tự cuối thì mặc định chạy hết chuỗi
print(s[1:])
# s[1:6]: từ vị trí index 1 đến vị trí index số 5 (tính cả index số 5)
print(s[1:6])
# s[:]: Lấy tất cả các phần tử (dùng cho trường hợp muốn tạo copy)
print(s[:])
# s[1:2]: Lấy 1 phần tử
print(s[1:2])
# s[1:1]: Không lấy phần tử nào cả => lấy ra chuỗi rỗng
print(s[1:1])

# Casting a number to string, dùng str()
decade = str(20.05)
print(type(decade))
print(decade)

# Các cách kiểm tra kiểu
# 1. type()
# 2. type() ==
# 3. isinstance(...,...)

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# function constructor str()
subject = str("mathematic")
print(type(subject))
print(type(subject) == str)
print(isinstance(subject, str))

# Multiple lines
# Để có nhiều dòng dùng 3 lần '' hoặc 3 lần ""
multilines = """
    Dòng trên
    Tôi tên là Công Nghĩa Hiếu
    Công
    Nghĩa
    Hiếu
    Dòng dưới
    HEHE     """

# 1 số str method
# print(multilines.lower())
# print(multilines.upper())
# print(multilines.title())
# print(multilines.capitalize())
# print(multilines.strip())
# print(multilines.lstrip())
# print(multilines.rstrip())
# print(multilines.replace('Công', 'Công vippro'))
