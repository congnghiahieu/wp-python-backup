users = ["Hieu", "Hai", "Hiep", "Trung"]

data = ["Trung", 2003, True]

empty_list = []

nums = [4, 42, 78, 5, 1, 4]

# List func constructor
newlist = list([1, 2, 3, 4, 10, 3])

# Để copy 1 list:
# Cách 1: dùng method list.copy() (shallow copy)
# Cách 2: copyNum = list(oldNum)
# Cách 3: copyNum = oldNum[:]

numscopy = nums.copy()
mynum = list(nums)
mycopy = nums[:]
