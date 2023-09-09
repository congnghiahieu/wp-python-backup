band = {
    "vocals": "Plant",
    "guitar": "Page",
    1: "Number one",
    "last": "This is last thing",
    1: "Number one two times",
}
band2 = dict(vocals="Plant", guitar="Page", o="OOO")

# list, dict, set đều là reference nên:
# newband = oldband => Không phải là copy mà là 2 biến tham chiếu tới cùng 1 vùng nhớ

# list.copy() hay dict.copy() đều là shallow copy
newband = band.copy()

# Dùng dict func constructor
newband2 = dict(band)  # shallow copy

# Nested dict ~ Nested object
member1 = {"name": "Hieu", "age": 20}
member2 = {"guitar": "Page", "last": "This is the last value"}
member3 = {"member1": member1, "member2": member2}
print(member3)
print(member3["member1"]["name"])
