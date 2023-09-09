x = True,
y = False,
z = True,

# not ~ !
# and ~ &&
# or ~ ||

# 🔸 Falsy Values

# Sequences and Collections:
# 
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty ranges range(0)

# Numbers
# 
# Zero of any numeric type.
# Integer: 0
# Float: 0.0
# Complex: 0j

# Constants
# 
# None
# False

# Truthy values include:
# 
# Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
# Numeric values that are not zero.
# True

# Toán tử phủ định
notX = not x
notY = not y
notZ = not z
print(notX)
print(notY)
print(notZ)

x and y
# Toán tử và "and"
# Toán tử "and" sẽ xem giá trị của x. Nếu x là đúng thì xem tiếp giá trị của y. Nếu x là sai thì lập tức trả về giá trị của x. Nếu check đến cuối không có cái nào sai thì trả về giá trị cuối cùng
# => Vị trí là quan trọng


x or y
# Toán tử và "or"
# Toán tử "or" sẽ xem giá trị của x. Nếu x là đúng thì lập tức trả về giá trị của x. Nếu x là sai thì xem tiếp giá trị của y. Nếu check đến cuối không có cái nào đúng thì trả về giá trị cuối cùng
# => Vị trí là quan trọng

print(0 or 1) # 1
print(False or 'hey') # 'hey'
print('hi' or 'hey') # 'hi'
print([] or False) # False
print(False or []) # []
