# Tuple: Bộ
# 1 bộ là cố định (immutable) tức là không thể thêm bớt sửa giá trị bên trong, không thể thay đổi thứ tự các phần tử
mytuple = tuple(("Dave", 42, True))
print(type(mytuple))

anothertuple = (1, 2, 4, 8, 16, 2, 3, 4)

# Tuple cũng có thể truy cập giá trị bằng index
print(f"1: {mytuple[0]}, 2: {mytuple[1]}, 3:{mytuple[2]} ")

# Tuple cũng có thể lấy được len (số lượng phần tử của tuple)
print(f"len: anothertuple {len(anothertuple)}")

# Tuple cũng có thể range slicing
print(anothertuple[1:3])

# Tạo 1 bộ gọi là packing
# 1 bộ có thể được unpacking (giống như destructuring)
# Chú ý khi unpacking: tuple có bao nhiêu giá trị thì phải unpack ngần đấy biến nếu không sẽ bắn lỗi
# VD:
# tuple = (one, two, three)
# (one, two) = tuple
# Dấu * giống ... (rest operator) trong destructuring để lấy các giá trị còn lại và lưu vào list

# sometuple = (1,2,3)
# (one, two) = sometuple # Bắn lỗi

# Unpack 1 tuple
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)  # hey là list vì tuple đã bị unpacking

# Tuple chỉ có thể được sort bằng hàm sorted (global, tạo ra 1 tuple mới)
print(sorted(anothertuple, reverse=True))

# Tuple có thể được nối để tạo ra 1 tuple mới. Vì tính chất immutable nên sẽ chỉ có thể tạo ra tuple mới
# Không thể: mytuple += ("new", "value")
# Có thể: newtuple = mytuple + anothertuple
newtuple = mytuple + anothertuple
print(newtuple)

# Tuple method
# method tuple.count(value) để đếm số lần xuất hiện của "value" trong tuple
print(anothertuple.count(2))

# method tuple.index(value) trả về index của 1 value cần tìm vị trí
# Bắn ra lỗi nếu không tìm thấy
print(mytuple.index(42))  # 0

# 1 tuple (immutable) có thể được cast về 1 list (mutable)
# 1 list (mutable) có thể được cast về 1 tuple (immutable)

newlist = list(mytuple)  # ('Dave', 42, True) => ['Dave', 42, True]
newlist.append("Gray")
newtuple = tuple(newlist)  # ['Dave', 42, True, 'Gray'] => ('Dave', 42, True, 'Gray')
print(newtuple)
