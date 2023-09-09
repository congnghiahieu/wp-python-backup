# List compressions

# Khỏi tạo list bằng for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

# Khởi tạo list bằng range
list1 = list(range(5, 10))
list2 = list(range(0, 10, 3))
list3 = list(range(-10, -100, -30))
print(list1)
print(list2)
print(list3)
