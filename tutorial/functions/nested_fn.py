# Hàm cha lồng hàm con
# 1 hàm con được định nghĩa trong 1 hàm thì chỉ có scope ở trong hàm cha đó


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)
    return


talk("My name is Công Nghĩa Hiếu")

# Sử dụng biến của hàm cha (không phải biến global)
# Dùng keyword "nonlocal"
# Nếu ở trong hàm con ta định nghĩa lại 1 biến "a" đã xuất hiện ở hàm cha, thì hàm con sẽ sử dụng giá trị của biến "a" được định nghĩa ở hàm con (VD bên dưới: count = 0)
# Nếu ở trong hàm con, không định nghĩa 1 biến "a" đã xuất hiện ở hàm cha mà vẫn muốn sử dụng. Thì phải sử dụng keyword "nonlocal" (VD bên dưới)
# Nếu không sử dụng nonlocal thì sẽ bị bắn lỗi (VD bên dưới: thử comment "nonlocal count")


def count():
    count = 10

    def increment():
        # count = 0
        nonlocal count
        count = count + 1
        print(count)

    increment()


count()
