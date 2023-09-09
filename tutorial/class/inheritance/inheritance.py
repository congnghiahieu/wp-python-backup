# Inheritance
from typing import List


class Employee:
    """
    - 1 class có thể kế thừa từ nhiều class. VD: class DerivedClassName(Base 1, Base 2, Base 3):
    - Khi runtime, nếu cần truy cập 1 biến, sẽ bắt đầu tìm kiếm ở chính class đó xem có biến đó không. Nếu tại chính class đó không có sẽ chuyển sang tìm kiếm ở class cha (ở class cha cũng xảy ra tương tự nếu class cha cũng được kể thừa từ 1 class "ông")
    - Derived class can extend or override method of their base class
    - Chú ý: Trong Python, class con có kế thừa lại constructor của class cha (Class con hoàn toàn có thể có 1 constructor riêng nhưng bắt buộc phải gọi super())
    """

    """ 
    Python có 2 phương thức built-in:
    - isinstance()
    - issubclass()
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

    @classmethod
    def get_ceo(cls):
        return cls.CEO_NAME


class Developer(Employee):
    salary_rate = 1.55

    def __init__(self, name: str, age: int, base_salary: float, prog_lang: str) -> None:
        super().__init__(name, age, base_salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    salary_rate = 2

    def __init__(
        self, name: str, age: int, base_salary: float, employees: List[Employee] = None
    ) -> None:
        super().__init__(name, age, base_salary)
        self.employees: List[Employee] = []
        if employees is not None:
            self.employees = employees

    def add_emp(self, emp: Employee):
        if emp not in self.employees:
            self.employees.append(emp)

    def rm_emp(self, emp: Employee):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for i, emp in enumerate(self.employees):
            print(f"Emp {i+1} --> {emp.name}")


# Sử dụng Inheritance
emp_1 = Employee("A", 20, 1000)
dev_1 = Developer("B", 30, 2000, "Python")
mng_1 = Manager("C", 40, 3000)
print(mng_1.cal_final_salary())
mng_1.add_emp(emp_1)
mng_1.add_emp(dev_1)
mng_1.print_emps()

# Sử dụng isinstance, isssubclass
print(f"mng_1 is instance of Employee: {isinstance(mng_1, Employee)}")
print(f"mng_1 is instance of Developer: {isinstance(mng_1, Developer)}")
print(f"mng_1 is instance of Manager: {isinstance(mng_1, Manager)}")
print(f"Manager is subclass of Employee: {issubclass(Manager, Employee)}")
print(f"Manager is subclass of Developer: {issubclass(Manager, Developer)}")
