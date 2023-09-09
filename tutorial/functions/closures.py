# Closure tương tự JS
# Điểm khác, muốn sử dụng biến ở hàm cha thì phải thêm keyword "nonlocal" ở hàm con


# Ví dụ 1:
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


increment = counter()
print(increment())  # 1
print(increment())  # 2
print(increment())  # 3


# Ví dụ 2: 2 hàm closure cùng access vào 1 biến global kiểu nguyên thuỷ đưới dạng tham số truyền vào
# Vì biến là kiểu nguyên thuỷ: int, float, str nên khi truyền vào hàm sẽ là pass by value
def coin_manipulate(name, coins):
    def play_game():
        nonlocal coins
        coins -= 1
        print(f"{name} has {coins} coins left.")

    return play_game


coins = 10
hieu = coin_manipulate("Hieu", coins)
dat = coin_manipulate("Dat", coins)
hieu()
hieu()
dat()


# Ví dụ 3: 2 hàm closure cùng access vào 1 biến global kiểu phức tạp (dict, list) đưới dạng tham số truyền vào
# Vì biến là kiểu phức tạp: dict, list, ... nên khi truyền vào hàm sẽ là pass by reference
def todo_list_manipulate(name: str, todo_list: list):
    def add_todo(todo: str):
        nonlocal todo_list
        todo_list.append(todo)
        print(f"{name} add {todo}")
        print(todo_list)

    return add_todo


todo_list = []
thieu = todo_list_manipulate("Thieu", todo_list)
cuong = todo_list_manipulate("Cuong", todo_list)
thieu("Thi MMT")
cuong("Trong thi MMT")
