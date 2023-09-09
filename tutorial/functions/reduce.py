# Để sử dụng reduct phải import
from functools import reduce


expenses = [("Dinner", 80), ("Car repaired", 120)]

# Without reduce
sum_without = 0
for expense in expenses:
    sum_without += expense[1]
print(sum_without)

# With reduce
# Chấp nhận 1 lambda gồm 2 biến đầu vào (accum, value): biến 1 là accumulated value, biến 2 là value
# Có thể thêm tham số thứ 3 là initial value
# Nếu có initial thì biến đầu tiên được duyệt là iterable[0] (value)
# Nếu không có initial thì iterable[0] sẽ là initial (accum), sẽ duyệt từ iterable[1] (value)

sum_with_initial = reduce(lambda accum, value: accum + value[1], expenses, 0)
print(sum_with_initial)

sum_with_reduce = reduce(lambda accum, value: accum[1] + value[1], expenses)
print(sum_with_reduce)
