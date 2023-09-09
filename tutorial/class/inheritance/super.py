""" 
- Chú ý: Trong Python, class con có kế thừa lại constructor của class cha (Class con hoàn toàn có thể có 1 constructor riêng nhưng bắt buộc phải gọi super())
- super(): hiểu đơn giản là tạo ra 1 đối tượng của class cha
- super().__init__(...): để gọi hàm khởi tạo của class cha (1 class con nếu có override lại constructor thì bắt buộc phải gọi super().__init__(...) của class cha)
- super().other_method(): để gọi các phương thức của class cha
"""


class Vehicle:
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.year = year

    def intro(self):
        print(f"{self.name} made in {self.year}")


class Car(Vehicle):
    """Car không định nghĩa lại hàm __init__ nên mặc định sẽ kế thừa __init__ từ class cha"""

    def intro(self):
        print(f"This car name is {self.name}, made in {self.year}")


class Motorbike(Vehicle):
    """Motorbike không định nghĩa lại hàm __init__ nên mặc định sẽ kế thừa __init__ từ class cha"""

    def intro(self):
        print(f"This motorbike name is {self.name}, made in {self.year}")


vehicle = Vehicle("Normal vehicle", 2000)
vehicle.intro(),
car = Car("Lambo", 2023)
car.intro()
motorbike = Motorbike("Suzuki", 2020)
motorbike.intro()


class Airplane(Vehicle):
    """
    Ariplane định nghĩa lại hàm __init__ nên phải gọi super().__init__(...) của class cha để đảm bảo đầy đủ tính chất của class cha.

    Phải đảm bảo super().__init__() phải được gọi đầu tiên
    """

    def __init__(self, name: str, year: int, power: float, speed: float) -> None:
        super().__init__(name, year)
        self.power = power
        self.speed = speed

    def intro(self, greeting_str: str) -> None:
        """Gọi hàm của class cha"""
        super().intro()

        print(
            f"{greeting_str}. This is {self.name} airplane with {self.speed} km/h and {self.power} power, made in {self.year}"
        )


airplane = Airplane("Boeing 747", 2023, 100.100, 350.5)
airplane.intro("Welcome")
