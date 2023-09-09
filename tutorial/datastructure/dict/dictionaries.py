# Dictionary giống object trong JS, Map trong JAVA

# Khi khởi tạo bằng {}:
# key có thể nhận là 1 chuỗi hoặc 1 số
# Nếu có có key lặp lại thì sẽ lấy giá trị của key mới nhất

# Khi khởi tạo bằng dict
# key chỉ có thể nhận là 1 tên biến hợp lệ (không phải có số, reserved keyword, ...)
# Không thể có trường hợp tên biến (tên key lặp lại)
# VD: band2 = dict(vocals="Plant", guitar="Page", o="OOO", o="") => bắn lỗi

band = {
    "vocals": "Plant",
    "guitar": "Page",
    1: "Number one",
    "last": "This is last thing",
    1: "Number one two times",
}
band2 = dict(vocals="Plant", guitar="Page", o="OOO")

print(band)
print(band2)
print(type(band))
print(len(band))  # Độ dài là có bao nhiêu key / value pairs trong dict

# Access items
# Truy cập bằng [key]
print(band["guitar"])
print(band["vocals"])
print(band[1])

# Truy cập bằng method dict.get(key)
print(band.get("guitar"))
print(band.get("vocals"))
print(band.get(1))

# Với những key không tồn tại sẽ trả về NoneType (không phải trả về chuỗi "None")
print((band.get(2)))  # None
print(type(band.get(2)))  # <class 'NoneType'>

# Thay đổi giá trị cho key. Nếu key đã tồn tại thì update, nếu key chưa tồn tại thì tạo mới
band["guitar"] = "New guitar"
band["new"] = "New value"
print(band)
# Sử dụng method dict.update({key: value})
band.update({"last": "Not last thing this time"})
band.update({"pizza": " "})
print(band)

# Dict method

# Tạo ra 1 dict mới với tập key trong list, và tất cả các key có giá trị bằng value
print(band.fromkeys([1, 2, 3, 4], 10))

# Lấy ra dict item: list of key / value pairs as tuples
print(band.items())
print(type(band.items()))
print(("vocals", "Plant") in band.items())

# Lấy ra keys as list
print(band.keys())
# Kiểm tra keys có ở trong dict hay không
print(2 in band.keys())  # như nhau
print(1 in band)  # như nhau

# Lấy ra values as list
print(band.values())
# Kiểm tra values có ở trong dict hay không
print("Page" in band.values())

# pop by key. If the key is not found, return the default if given (second arg); otherwise, raise a KeyError.
# Nếu tìm thấy thì trả về value
print(band.pop("guitar"))
print(band)
print(band.pop(2, "Not found"))
print(band)
# pop the last item. Trả về 1 tuple (key, value)
print(band.popitem())
print(band)

# Delete and clear

# Xoá 1 key khỏi dict ~ tương tự pops
band["ball"] = "football"
del band["ball"]

# Clear key / value pair in dict
band2.clear()
print(band2)
# Delete 1 dict. Không thể truy cập được nữa
del band2
