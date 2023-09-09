users = ["Hieu", "Hai", "Hiep", "Trung"]

data = ["Trung", 2003, True]

empty_list = []

# Kiểm tra xem 1 giá trị có nằm trong list hay không, dùng keyword "in"
print("Hieu" in users)
print("Trung" in data)
print(12 in empty_list)

# Lấy ra 1 giá trị trong list bằng index. Chú ý: lấy phần tử cuối cùng phần index -1, gần cuối -2
print(users[0])
print(data[-1])
print(users[-2])
# print(empty_list[1]) # Sẽ bị lỗi index out of range

# Lấy ra index của 1 giá trị
# Nếu giá trị không có trong list thì sẽ tung lỗi
print(users.index("Hieu"))
# print(users.index(True)) # Nên kiểm tra giá trị có trong list hay không bằng keyword "in"

# Lấy ra giá trị theo range
# users[0:2]: Lấy giá trị từ index 0 đến index 1 (lấy cả index 1)
print(users[0:2])
# users[1]: Lấy từ index 1 cho đến hết
print(users[1:])

# Kiểm tra độ dài của mảng
print(len(users))
print(len(data))
print(len(empty_list))

# Unpack 1 list
(one, two, *three) = [1, 2, 3]
print(one)
print(two)
print(three)

# Thêm giá trị của cuối mảng, dùng method "appped" (không có method "push")
users.append("Duy")
print(users)

# Nối mảng: nối 1 list mới hoặc 1 list đã tồn tại
# Cách 1: dùng += ["new", "list"]
# Cách 2: dùng method extend: list.extend(["new", "list"])

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# Chèn 1 giá trị
# Thêm "HiHi" vào vị trí index 0, giá trị tại index 0 cũ bị lùi lại thành index 1
users.insert(0, "HiHi")
print(users)

# Chèn 1 list mới vào vị trí
# Sau khi chèn, giá trị tại index 0 sẽ là 1 list (list trong list ~ mảng 2 chiều)
users.insert(0, ["HaHa", "Hehe"])
print(users)  # [["HaHa", "Hehe"], "HiHi", "Hieu", ...]

# Chèn nhiều giá trị bằng range index
# users[2:2]: Chọn vị trí index số 2, nhưng không lấy phần tử nào cả, thêm vào từ index 2 2 giá trị "Minh" (index 2) và "Tuan" (index 3). Các phần tử cũ bị lùi lại
# Giống như phép slice
users[2:2] = ["Minh", "Tuan"]
print(users)

# Thay thế giá trị bằng range
# users[0:1]: lấy ra phần tử tại index 0, thay thế index 0 bằng "Hung", "Huy" là index 1 mới, index 1 cũ bị lùi lại
# Giống như phép slice
users[0:1] = ["Hung", "Huy"]
print(users)

# Remove 1 phần tử theo giá trị và không trả về gì
# Nếu phần tử không tồn tại trong list thì bắn lỗi => nên kiểm tra trước bằng keyword "in"
users.remove("HiHi")
print(users)

# Remove 1 phần từ theo index
# Nếu không truyền tham số thì sẽ pop và trả về phần tử cuối cùng
# Nếu truyền index thì sẽ pop và trả về phần tử tại index
# Nếu index không tồn tại thì bắn lỗi
print(users.pop())
print(users)
print(users.pop(0))
print(users)

# Remove 1 phần từ bằng keyword "del"
del users[0]
print(users)

# Remove nhiều phần tử trong range bằng keyword "del"
del users[0:2]
print(users)

# Clear list, dùng method list.clear() => list rỗng
users.clear()
print(users)

# Xoá biến list bằng keyword "del". Biến list sẽ bị xoá hoàn toàn và không thể gọi lại được
# del data
# print(data) # Sẽ bắn lỗi tại đây. Lỗi: 'name "data" is not defined'
