import uuid
from typing import List
from dataclasses import dataclass, field


def generate_random_id():
    return str(uuid.uuid4())[0:8]


@dataclass(frozen=True)
class Employee:
    """
    Chú ý khi gán default value cho attribute:
    - Nếu default value là primitive như str, int, float, bool thì không xảy ra vấn đề
    - Nếu default value là list, dict thì tất cả các instance được khởi tạo đều có email_addresses chỉ tới 1 list (1 địa chỉ duy nhất). Tức là tất cả các instance đều có email_addresses, nhưng tất cả attribute email_addresses này lại chỉ tới 1 list duy nhất
    - Cập nhật Python 3.10: dataclasses sẽ raise ValueError nếu khởi tạo giá trị mặc định là 1 mutable. Giá trị mặc định là 1 mutable bắt buộc phải sử dụng default_factory

    Để đảm bảo cho gán default value là reference, sử dụng field(default_factory=lambda: [])
    default_factory nhận tham số là 1 function không có tham số đầu vào

    Trong 1 số trường hợp ta muốn tự khởi tạo giá trị mặc định cho instance mà không muốn người sử dụng can thiệp, VD tạo ID
    Sử dụng: field(init=False) để không có giá trị khởi tạo khi tạo instance
    """

    """
    Khi muốn tạo attribute dựa trên giá trị của các attribute khác, sử dụng __post_init__
    """

    """
    Mới cập nhật Python 3.10:
    - kw_only: bool = False. Nếu bằng True thì chỉ có thể khởi tạo instance bằng keyword argument, không thể sử dụng positional argument
    - match_args: bool = True.
    - slots: bool = False. Nếu bằng True mặc đinh instance chỉ có các attribute như khi khởi tạo, không thì tuỳ tiện thêm attribute vào instance như: emp_1.smt = "Hello World". Dùng slots tránh việc thêm attribute linh tinh vào instance
    
    So sánh frozen và slots:
    frozen:
        - Không thể thêm attribute mới cho instance
        - Không thể gán lại giá trị cho attribute sau khởi tạo
        - Muốn gán thêm hoặc gán lại giá trị thì sử dụng object.__setattr__(self, '...', ...)
    slots:
        - Không thể thêm attribute mới cho instance
        - Có thể gán lại giá trị cho attribute sau khởi tạo
        - Truy cập nhanh hơn so với lưu attribute vào dict của class thông thường

    """

    name: str
    address: str
    active: bool = False
    email_addresses: List[str] = field(default_factory=lambda: [])
    id: str = field(init=False, default_factory=generate_random_id)
    description: str = field(init=False)

    def __post_init__(self):
        description = f"{self.id} - {self.name} - {self.address} - {self.active}"
        self.description = description

        # Nếu frozen=True
        # object.__setattr__(self, "description", description)


emp_1 = Employee("A", "VN", True, ["adefault@email.com"])
emp_2 = Employee("B", "US")

# Nếu slots = True thì không thể thêm attribute tuỳ tiện vào instance
# emp_1.smt = "Hello World"

emp_1.email_addresses.append("a@email.com")
emp_2.email_addresses.append("b@email.com")

print(emp_1)
print(emp_2)
