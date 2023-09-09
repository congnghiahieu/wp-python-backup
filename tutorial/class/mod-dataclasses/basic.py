from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Employee:
    """
    Các tham số của dataclass:
    init: bool = True - Tự động tạo hàm __init__
    repr: bool = True - Tự động tạo hàm __repr__
    eq: bool = True - Tự động tạo hàm __eq__
    order: bool = False - Tự động tạo các hàm '__lt__', '__le__', '__gt__', '__ge__'
    unsafe_hash: bool = False - Tự động thêm __hash__
    frozen: bool = False - Nếu True, các attribute sau khi khởi tạo không thể được gán lại giá trị
    match_args: bool = True
    kw_only: bool = False
    slots: bool = False
    """

    """
    Có thể thêm default value cho attribute
    """

    """
    Muốn chỉ rõ sorting theo giá trị nào thì ta thêm attribute sort_index và hàm __post_init__, VD:

    sort_index: int = field(init=False, repr=False)
    def __post_init__(self):
        self.sort_index = self.base_salary

    Phải chỉ rõ sort_index không phải là thuộc tính của class, ta sử dụng field(init=False). Để không hiện thị sort_index khi print (gọi __repr__), ta thêm repr=False, VD: field(init=False, repr=False)
    Chi rõ sort theo tiêu chí nào sử dụng __post_init__
    """

    """
    Có thể sử dụng frozen=True để tránh việc các attribute có thể bị gán lại giá trị.
    Tuy nhiên sử dụng frozen=True sẽ không thể thực hiện __post_init__ để gán self.sort_index. Cách khắc phục:

    object.__setattr__(self, "sort_index", self.base_salary)
    """
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    base_salary: float
    default_weekday: int = 6

    def __post_init__(self):
        # self.sort_index = self.base_salary

        """Sử dụng nếu đồng thời sort và frozen"""
        object.__setattr__(self, "sort_index", self.base_salary)


emp_1 = Employee("A", 20, 3000)  # init = True
emp_2 = Employee("B", 30, 2000)  # init = True
emp_3 = Employee("B", 30, 2000)  # init = True

print(emp_1)  # repr = True
print(id(emp_2))
print(id(emp_3))
print(emp_2 == emp_3)  # eq = True
print(emp_1 > emp_3)  # order = True
