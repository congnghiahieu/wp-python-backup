# Biến được định nghĩa global thì tất cả các hàm có thể truy cập được

# Định nghĩa lại 1 biến (ở scope cha)
# Nếu ở scope cha cho có định nghĩa 1 biến a = 8
# Và ở scope con ta định nghĩa lại 1 biến  a = 10
# Ở trong phạm vi hàm con thì khi gọi a thì a sẽ bằng 10
# Ở ngoài phạm vi hàm con thì khi gọi a thì a sẽ bằng 8
# Ví dụ bên dưới

age = 8  # global


def test():
    age = 10
    print(age)  # 10


print(age)  # 8
test()  # 8


# global keyword
# Ví dụ trong TH dưới: count là 1 biến global
# Nếu ở trong hàm parent ta chỉ đọc biến count thì không vấn đề gì
# Nếu ở trong hàm parent ta "count = 2" thì tức là tạo 1 biến count mới trong phạm vi local
# Nếu "count += 1" sẽ xảy ra lỗi bởi vì "count += 1" đã khởi tạo 1 biến count mới (phạm vị local) nhưng không gán giá trị khởi tạo nên không thể += 1
# Muốn chỉnh sửa giá trị của biến count (có phạm vi global) ta sử dụng keyword "global"
# Khai báo (khai báo lại) 1 biến count lấy từ global
# Có thể sử dụng để đọc, chỉnh sửa như bình thường

count = 1  # global


def parent():
    color = "blue"
    # count += 1 # Sẽ xuất hiện lỗi "UnboundLocalError: cannot access local variable 'count' where it is not associated with a value"
    # count = 3 # Khai báo 1 biến count mới. Biến count ở phạm vi global vẫn có giá trị bằng 1
    global count
    count += 1  # Biến count ở global đã có giá trị bằng 2
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting("Hiếu")


parent()
print(count)

# nonlocal keyword
# Biến được định nghĩa ở hàm cha thì hàm con phải sử dụng keyword "nonlocal" thì mới có thể chỉnh sửa được (vẫn có thể chỉ đọc được) (nếu không muốn định nghĩa lại). Nếu không sử dụng "nonlocal" mà vẫn thực hiện chỉnh sửa giá trị (nếu chỉ đọc thì vẫn OK) (không định nghĩa lại) thì sẽ bắn lỗi
# Biến được định nghĩa ở hàm con thì hàm cha không đọc được


def level_1():
    color = "Yellow"

    def level_2():
        # Nếu khai báo 1 biến mới, thì không phải là biến "color" của level 1 nữa
        # color = "New color"

        # Nếu muốn thực hiện chỉnh sửa biến color ở phạm vi level_1
        nonlocal color
        color = "New color"

        # Nếu chỉ đọc thì vẫn được
        print(color)

    level_2()
    print(color)


level_1()
