""" Dog module
This module is for ...

End docs
"""


def increment(n):
    """Increment a number"""
    return n + 1


class Dog:
    """A class representing a dog"""

    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("Wolf!")


print(
    help(Dog)
)  # Để xem docs của 1 class, function trong module hoặc được import từ module khác
