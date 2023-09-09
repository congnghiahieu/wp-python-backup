# Property decorator - @property


class Employee:
    """
    @property: cung cấp getter, setter, deleter cho 1 property có thể được suy diễn từ property khác, VD: email, fullname

    Hàm được đánh @property sẽ được coi là getter
    Tạo setter bằng cách sử dụng @fullname.setter
    Tạo deleter (dành cho khi sử dụng del emp_1.fullname) bằng cách sử dụng @fullname.deleter

    """

    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @email.setter
    def email(self, new_email: str):
        first, last = new_email[0 : new_email.find("@email.com")].split(".")
        self.first = first
        self.last = last

    @email.deleter
    def email(self):
        self.first = ""
        self.last = ""

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, new_fullname: str):
        first, last = new_fullname.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = ""
        self.last = ""

    def __repr__(self) -> str:
        return f"{self.fullname} - {self.email}"


emp_1 = Employee("Cong", "Hieu")
emp_2 = Employee("Nguyen", "Hai")

del emp_1.email

print(emp_1.email)
print(emp_1.fullname)
print(emp_2.email)
print(emp_2.fullname)
