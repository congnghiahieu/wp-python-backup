# More about caching replacement policies: https://en.wikipedia.org/wiki/Cache_replacement_policies

from functools import cache, lru_cache

"""
@cache được sử dụng để ghi tham số đầu vào cho hàm, hữu dụng trong các trường hợp hàm tính toán tốn nhiều thời gian, phức tạp

@cache là 1 phiên bản không có giới hạn bộ nhớ của lru_cache. Tức là nếu bộ tham số đã từng xuất hiện 1 lần thì trong các lần sau sẽ được nhớ (bất kể khoảng cách từ lần gọi đầu tiên của bộ tham số đó tới lần thứ 2 gọi bộ tham số đó)
VD: Nếu tham số (1,2) được gọi vào lần thứ 1 của hàm multiply, lần thứ 10000 hàm multiply được gọi với tham số (1,2) thì sẽ được ghi nhớ
Vì @cache không có giới hạn bộ nhớ nên phải cẩn thận khi sử dụng, có thể gây ra tốn quá nhiều bộ nhớ vì cache quá lớn và cache quá lớn thì tốc độ cũng bị chậm đi

lru_cache là 1 phiên bản có giới hạn bộ nhớ. Lưu đến khi hết bộ nhớ được cấp thì xoá đi tham số 

"""


@cache
def multiply_nolimit_cache(x: int, y: int):
    print("Multiplying ...")
    return x * y


print(multiply_nolimit_cache(2, 1))
print(multiply_nolimit_cache(2, 2))
print(multiply_nolimit_cache(2, 3))
print(multiply_nolimit_cache(2, 4))
print(multiply_nolimit_cache(2, 5))
print(multiply_nolimit_cache(2, 6))
print(multiply_nolimit_cache(2, 7))
print(multiply_nolimit_cache(2, 8))
print(multiply_nolimit_cache(2, 9))
print(multiply_nolimit_cache(2, 10))
print(multiply_nolimit_cache(2, 1))

print("-------------------- LRU CACHE ---------------------- ")


@lru_cache(maxsize=10)
def multiply_lru_cache(x: int, y: int):
    print("Multiplying ...")
    return x * y


print(multiply_lru_cache(2, 1))
print(multiply_lru_cache(2, 2))
print(multiply_lru_cache(2, 3))
print(multiply_lru_cache(2, 4))
print(multiply_lru_cache(2, 5))
print(multiply_lru_cache(2, 6))
print(multiply_lru_cache(2, 7))
print(multiply_lru_cache(2, 8))
print(multiply_lru_cache(2, 9))
print(multiply_lru_cache(2, 10))
print(multiply_lru_cache(2, 1))
