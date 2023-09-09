users = [
    "Hieu",
    "Hai",
    "Hiep",
    "Bob",
    "Cao",
    "Trung",
    "Duong",
    "Edward",
    "Loyd",
    "Athena",
    "dave",
    "gray",
]

data = ["Trung", 2003, True]

empty_list = []

# Sử dụng list.sort() sẽ là in-place sort (sort ngay list, không trả ra list mới) và stable

# Chú ý: khi sort các kiểu dữ liệu thông thường như str, number thì tất cả phải cùng 1 kiểu dữ liệu
# Nếu có 2 kiểu dữ liệu int và str trong 1 list sẽ bắn lỗi
# Khi sort mặc định như này thì Uppercase sẽ được sắp xếp ở trước, lowwercase sau
users.sort()
print(users)
# data.sort() # => Bắn lỗi

# Python cũng hỗ trợ truyền callback
# truyền callback (comparator) cho hàm list.sort(key=callback)
# Ngoài ra còn có: list.sort(reverse=True) để đảo ngược thứ tự

users.sort(key=str.lower)
print(users)

users.sort(reverse=True)
print(users)

# Đảo ngược thứ tự trong list, dùng method list.reverse()
nums = [4, 42, 78, 5, 1, 4]
nums.reverse()
print(nums)

# Dùng global method "sorted" để not in-place sort (Trả về list mới)
print(sorted(nums, reverse=True))
print(nums)
