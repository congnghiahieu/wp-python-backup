from typing import Dict

""" 
More at: https://www.youtube.com/watch?v=WR7mO_jYN9g

Iterable: 1 container được coi là Iterable thì phải có dunder method __iter__, trong đó __iter__ trả về con trỏ duyệt. Có thể dùng container.__iter__() hoặc iter(container)

Iterator: 1 iterator được coi là Iterator nếu có dunder method __next__, trong đó __next__ trả về element tiếp theo, nếu hết element thì raise StopIteration. Có thể dùng iterator.__next()__ hoặc next(iterator)

VD:  for ele in mylist
Thì `in` sẽ trả về iterator của mylist (tức là gọi mylist.__iter__() hoặc iter(mylist)). Sau đó sẽ tiếp tục gọi iterator.__next() hoặc next(iterator) cho đến khi list hết element

Sequence: Iterable + Ordered, VD: list, tuple, str, bytes
"""

""" Ví dụ về dunder method __iter__ và __next__ """
usernames_1 = ("A", "B", "C")
iterator_1 = usernames_1.__iter__()
print(type(iterator_1))
print(iterator_1.__next__())
print(iterator_1.__next__())
print(iterator_1.__next__())
# Nếu vẫn tiếp tục gọi thì raise StopIteration
# print(iterator_1.__next__())

""" Ví dụ về built-in method iter và next """
usernames_2 = ("D", "E", "F")
iterator_2 = iter(usernames_2)
print(type(iterator_2))
print(next(iterator_2))
print(next(iterator_2))
print(next(iterator_2))
# Nếu vẫn tiếp tục gọi thì raise StopIteration
# print(next(iterator_2))

""" Tự tạo 1 Iterable class """


class TicketAgent:
    def __init__(self, holdings: Dict[str, int]) -> None:
        self.holdings = holdings

    def buy(self, name: str, quantity: int):
        self.holdings[name] = self.holdings.get(name, 0) + quantity

    def sell(self, name: str, quantity: int):
        self.holdings[name] = self.holdings.get(name, 0) - quantity

    def __iter__(self):
        return iter(self.holdings.items())


ticket_agent = TicketAgent(
    {
        "A": 10,
        "B": 20,
        "C": 30,
    }
)
ticket_agent.buy("A", 20)
ticket_agent.buy("A", 30)
ticket_agent.buy("B", 10)

for name, quantity in ticket_agent:
    print(f"{name}: {quantity}")
