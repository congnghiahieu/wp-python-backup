class Employee:
    """
    Class variable có thể access bằng 2 cách:
    - Thông qua class, VD: Employee.salary_rate
    - Thông qua chính instance, VD: self.salary_rate

    Class variable có phạm vi ở cả class và instance, nhưng:
    - Khi 1 instance được khởi tạo thì nó vẫn tham chiếu tới class variable chung của class
    - Nhưng nếu ta thực hiện gán, VD: emp_1.salary_rate = 1.55. Tức là ta đã tạo ra 1 biến salary_rate ở phạm vi của instance đó
    - Nếu ta thực hiện chỉnh sửa, VD: emp_1.salary_rate = 1.55. Thì emp_2.salary_rate và Employee.salary_rate vẫn bằng 1.42. Tức là sửa class variable ở trên phạm vi 1 instance không ảnh hướng tới instance khác hay class
    - Nếu ta thực hiện chỉnh sửa, VD: Employee.salary_rate = 1.55. Thì emp_1.salary_rate và emp_2.salary_rate sẽ bằng 1.55. Tức là sửa class variable ở trên phạm vi class thì sẽ ảnh hưởng tới instance của nó

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


emp_1 = Employee("A", 20, 1000)
emp_2 = Employee("B", 30, 2000)

# emp_1.salary_rate = 1.55
# Employee.salary_rate = 1.55

print(f"Emp 1: {emp_1.salary_rate}")
print(f"Emp 2: {emp_2.salary_rate}")
print(f"Employee class: {Employee.salary_rate}")
