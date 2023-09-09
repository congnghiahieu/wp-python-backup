# Có thể tự raise 1 Error (hoặc Exception)

try:
    raise KeyError
except KeyError as error:
    print("Catch error")
    print(error)


# Custom exception
# VD1: Đơn giản
class DocNotFoundException(Exception):
    """This is a custom Exception"""

    pass


# VD2: Custom Exception
class UserNotFoundException(Exception):
    def __init__(self, user_id: str | int, message: str) -> None:
        super().__init__(f"User with ID {user_id}: {message}")
