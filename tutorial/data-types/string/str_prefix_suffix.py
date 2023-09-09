# %s, %d, %f trong Python giống như %d, %f, %s ở các ngôn ngữ khác

# f để đánh dấu string có interpolate

# r là 1 prefix, để đánh dấu tất cả nội dung ở trong dấu "" hoàn toàn là chuỗi thuần

# u đánh dấu đây là string mang kí tự unicode

# b đánh dấu đây là string chuỗi byte

""" 
1. f string
- Không thể sử dụng if else, chỉ có thể sử dụng ternary statement
"""
first = "Cong"
last = "Hieu"
print(f"My name is {first} {last}")
fullname = f"My full name is {first} {last}"
print(fullname)
age = 25
print(f"Now I am {25 if age > 25 else 10} years old")

# 2. Sử dụng format method
# Sử dụng format method là 1 cách cũ (Deprecated) của f string
# Nếu thêm index vào trong {} thì có thể thay đổi thứ tự (index bắt đầu từ 0)

person = "Hieu"
money = "1$"
print("{} has {}".format(person, money))  # Hieu has 1$
print("{1} has {0}".format(person, money))  # 1$ has Hieu

# 3. %s giống như %d, %f, %s ở các ngôn ngữ khác
# Declaring a string variable
var1 = "Geek!"
var2 = "Geeks for Geeks"

# append multiple strings within a string
print("Hello %s Are you enjoying being at %s for preparations." % (var1, var2))

# Declaring string variables
str1 = "Understanding"
str2 = r"%s"  # r ở phía trước nên đây là text thuần
str3 = "at"
str4 = "GeeksforGeeks"

# concatenating strings
final_str = "%s %s %s %s" % (str1, str2, str3, str4)

# printing the final string
print("Concatenating multiple strings using Python '%s' operator:\n")
print(final_str)  # Understanding %s at GeeksforGeeks

# Declaring string variables with dictionary
dct = {"str1": "at", "str2": "GeeksforGeeks", "str3": "Understanding", "str4": r"%s"}

# concatenating strings
final_str = "%(str3)s %(str4)s %(str1)s %(str2)s" % dct

# printing the final string
print("Concatenating multiple strings using Python '%s' operator:\n")
print(final_str)  # Understanding %s at GeeksforGeeks
