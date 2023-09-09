# Set: tập hợp không có trùng lặp (dups)
# Chú ý: Trong set, True được coi là dup của 1, False được coi là dup của 0

# Khởi tạo
setnums = {2, 1, 6, 4, 3, 5, 6}
setnums2 = set((1, 2, 3, 4, 1123, 3, "String"))

print(setnums)
print(type(setnums2))
print(setnums2)

# Trong set không cho phép trùng lặp
myset = {1, True, 2, 3, 3, 4, False, 0}
print(
    myset
)  # {False, 1, 2, 3, 4}. 1 xuất hiện trước True nên được giữ lại. False xuất hiện trước 0 nên giữ lại

# Có thể check giá trị có nằm trong set hay không
# Nhưng không thể truy cập giá trị bằng index
print(2 in myset)

# Thêm giá trị, cập nhật giá trị cho set
myset.add(5)

# Method update, thêm phần tử cho set
# Method update chấp nhận 1 set khác, chấp nhận 1 list, chấp nhận 1 dict (sẽ lấy keys của dict), chấp nhập values của 1 dict (dict.value())

# With other set
moreset = {6, 7, 8, 5}
myset.update(moreset)
print(myset)
# With other dict
mydict = {
    1: "One",
    "Two": 2,
}
myset.update(mydict.keys())
myset.update(mydict.values())
print(myset)
# With other list
mylist = ["hieu", "cong", "nghia"]
myset.update(mylist)
print(myset)

# Merge 2 set to create new set
setone = {1, 2, 3, 4, 5}
settwo = {4, 5, 6, 7, 8}

mergedset = setone.union(settwo)
print(mergedset)

# Lấy phần giao
intersectedset = setone.intersection(settwo)
print(intersectedset)

# Lấy phần chỉ tồn tại ở set gọi hàm này
print(setone.difference(settwo))  # {1, 2, 3}

# Lấy phần khác nhau giữa 2 set (phần khác nhau ở cả set 1 và set 2)
print(setone.symmetric_difference(settwo))  # {1, 2, 3, 6, 7, 8}
