# map(), filter(), reduce()

# Map
numbers = [1, 2, 3, 4]


def double(a):
    return a * 2


three_times = lambda a: a * 3

result_two = map(double, numbers)
print(result_two)  # <map object at 0x00000154EA16AB30>
print(list(result_two))  # [2, 4, 6, 8]

result_three = map(three_times, numbers)
print(result_three)  # <map object at 0x000001F7E5CAB850>
print(list(result_three))  # [3, 6, 9, 12]

result_four = map(lambda a: a * 4, numbers)
print(result_four)  # <map object at 0x00000220691CB790>
print(list(result_four))  # [4, 8, 12, 16]
