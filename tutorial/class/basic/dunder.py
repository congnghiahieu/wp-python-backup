class Employee:
    """
    __repr__ (represent): là 1 dạng biểu diễn instance ở dạng dễ đọc hơn, thường được sử dụng với mục đích cho developer đọc, mục đích debuging, logging
    Convention cho __repr__: nên viết ở dạng Python code có thể copy and paste để reproduce được
    VD:
    def __repr__(self):
        return f"Employee({self.name}, {self.age}, {self.base_salary})"

    __str__ (string): là 1 dạng biểu diễn instance bằng string, dễ đọc hơn, thường được sử dụng với mục đích cho end user đọc
    Convention cho __repr__: nên viết ở dạng human-readable
    VD:
    def __str__(self):
        return f"Employee information:\n{self.name} - {self.age} - {self.base_salary}"

    Khi gọi built-in method:
    repr(): thì sẽ gọi tới __repr__ của instance
    str(): thì sẽ gọi tới __str__ của instance. Nếu class của instance không định nghĩa __str__ thì gọi tới __repr__
    id(): trả về địa chỉ trong RAM của instance
    print(): sẽ gọi tới __str__ của instance. Nếu class của instance không định nghĩa __str__ thì sẽ gọi tới __repr__ (__repr là 1 fallback của __str__). Nếu class của instance không định nghĩa __repr__ thì sẽ gọi tới hàm global id() để lấy ra địa chỉ trong RAM của instance
    """

    """
    __len__: Khi dùng len(instance) thì sẽ gọi đến __len__
    """

    salary_rate = 1.42

    def __init__(self, name: str, age: int, base_salary: float) -> None:
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def full_info(self):
        return f"{self.name} - {self.age} - {self.base_salary}"

    def cal_final_salary(self):
        return self.base_salary * self.salary_rate

    def __repr__(self) -> str:
        return f"Employee({self.name}, {self.age}, {self.base_salary})"

    def __str__(self):
        return f"Employee information: {self.name} - {self.age} - {self.base_salary}"

    def __len__(self) -> int:
        return len(self.name) * self.age


emp_1 = Employee("A", 20, 1000)
emp_2 = Employee("B", 30, 2000)

print(id(emp_1))
print(repr(emp_1))
print(str(emp_1))
print(len(emp_1))
print(emp_1)
