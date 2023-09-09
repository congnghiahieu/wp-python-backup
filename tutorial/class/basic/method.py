""" 
Regular method
Class method
Static method
"""

import datetime


class Employee:
    """
    - Regular method - instance method, là hàm nhận tham số đầu tiên là self (self là con trỏ, trỏ tới chính instance)
    """

    """ 
    - Class method - được đánh decorator @classmethod, là hàm nhận tham số đầu tiên là cls (cls là con trỏ, trỏ tới chính class)
    - Class method có thể dược gọi bằng 2 cách: emp_1.set_salary_rate() hoặc Employee.set_salary_rate() 

    - Class method được ứng dụng để tạo nhiều hàm khởi tạo cho class
    - Chú ý: các hàm khởi tạo bằng method thường được bắt đầu bằng from (convention)
    VD:
    @classmethod
    def from_string(cls, emp_str: str):
        name, age, base_salary = emp_str.split("-")
        return cls(name, age, base_salary)
    """

    """ 
    - Static method - là hàm không nhận tham số đầu tiên nào (giống như 1 hàm bình thương)
    - Convention: Nếu hàm không truy cập đến self (instance) hoặc cls (class) thì nên đánh decorator @staticmethod
    VD:
    @staticmethod
    def is_workday(day: Datetime):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    """

    salary_rate = 1.42
    CEO_NAME = "HIEU"

    def __init__(self, name: str, age: int, base_salary: float) -> None:
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def full_info(self):
        return f"{self.name} - {self.age} - {self.base_salary}"

    def cal_final_salary(self):
        return self.base_salary * self.salary_rate

    def get_ceo(self):
        return Employee.CEO_NAME

    def get_self(self):
        """self: Self@Employee"""
        print(f"Self: {self}")

    @classmethod
    def get_class(cls):
        """cls: type[Self@Employee]"""
        print(f"Class: {cls}")

    @classmethod
    def set_salary_rate(cls, amount: float):
        cls.salary_rate = amount

    @classmethod
    def from_string(cls, emp_str: str):
        """More way to construct new instance by using @classmethod"""
        name, age, base_salary = emp_str.split("-")
        return cls(name, int(age), float(base_salary))

    @staticmethod
    def is_workday(day: datetime.datetime):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("A", 20, 1000)
emp_2 = Employee("B", 30, 2000)


def a():
    return Employee


emp_1.get_self()
emp_1.get_class()

# emp_1.set_salary_rate(1.55)
Employee.set_salary_rate(1.55)

print(f"Emp 1: {emp_1.salary_rate}")
print(f"Emp 2: {emp_2.salary_rate}")
print(f"Employee: {Employee.salary_rate}")

# Ứng dụng @classmethod để có nhiều cách khởi tạo
emp_from_str = Employee.from_string("C-40-3000")
print(emp_from_str.__dict__)

# Sử dụng static method
now = datetime.datetime.now()
print(f"{now} is{'' if Employee.is_workday(now) else ' not'} workday")
