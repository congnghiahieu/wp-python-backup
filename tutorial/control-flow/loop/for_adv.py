names = ["Dave", "Sara", "Hieu", "Hai", "John"]

# Lấy index Cách 1
for i in range(len(names)):
    print(f'index {i}: value {names[i]}')

# Lấy index Cách 2
# enumerate sẽ trả về 1 tuple gồm 2 giá trị (index, value)
# Ta phải unpack theo đúng thứ tự để lấy được index
for (index, value) in enumerate(names):
    print(f'{index}: {value}')

# For loop through a dict
users = {
    'Quinn': 'active',
    'Eleonore': 'inactive',
    'Bob': 'active'
}

# Xoá các user active
users_copy = users.copy()
for (user, status) in users.items():
    if status == 'active':
        del users_copy[user]
print(users_copy)
print(users)

# Lấy ra các users active
active_users = {}
for (user,status) in users.items():
    if (status == 'active'):
        active_users[user] = status
print(active_users)

# Khởi tạo list bằng range
list1 = list(range(5,10))
list2 = list(range(0,10,3))
list3 = list(range(-10,-100,-30))
print(list1)
print(list2)
print(list3)