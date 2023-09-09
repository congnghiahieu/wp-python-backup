# For loop hoạt động bình thường với break và continue

# For loop through list

names = ["Dave", "Sara", "Hieu", "Hai", "John"]

for name in names:
    print(name)
    
# For loop through a str
for c in "Công_Nghĩa_Hiếu_13_12_2003":
    print(c)

# For in range(n)
# Nếu không có kí tự bắt đầu thì mặc định duyệt từ 0 đến n - 1
for x in range(4): # 0 1 2 3
    print(x)
# Nếu có kí tự bắt đầu thì duyệt từ start đến n - 1
for x in range(1,4): # 1 2 3
    print(x)
# Range có thể chỉ định đủ 3 giá trị cho range(start, end, increment)
# VD: muốn bắt đầu tại số 0, kết thúc tại 100 (0-100) (tính cả 100), bước nhảy là 5 => range(0, 101, 5)
# Hoàn toàn có thể thêm for else như while else
for x in range(0,101,5):
    print(x)
else:
    print("For loop is over 🤔")

# Nested loop
actions = ["play", "run", "sleep"]

for name in names:
    for action in actions:
        print(name + " " + action)