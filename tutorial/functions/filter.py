numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def isEven(n):
    return n % 2 == 0


isOdd = lambda n: n % 2 == 1

result_even = filter(isEven, numbers)
print(result_even)  # <filter object at 0x000001DA2B2CB7F0>
print(list(result_even))  # [2, 4, 6, 8, 10]

result_odd = filter(isOdd, numbers)
print(result_odd)  # <filter object at 0x000001DA2B2CB790>
print(list(result_odd))  # [1, 3, 5, 7, 9]

result_divided_by_20 = filter(lambda n: 20 % n == 0, numbers)
print(result_divided_by_20)  # <filter object at 0x000001E75484B6D0>
print(list(result_divided_by_20))  # [1, 2, 4, 5, 10]
