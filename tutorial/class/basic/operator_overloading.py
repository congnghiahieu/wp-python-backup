# Operator overloading
# More about operator overloading: https://www.geeksforgeeks.org/operator-overloading-in-python/


class Dog:
    """
    Binary Operator:
    +	__add__(self, other)
    –	__sub__(self, other)
    *	__mul__(self, other)
    /	__truediv__(self, other)
    //	__floordiv__(self, other)
    %	__mod__(self, other)
    **	__pow__(self, other)
    >>	__rshift__(self, other)
    <<	__lshift__(self, other)
    &	__and__(self, other)
    |	__or__(self, other)
    ^	__xor__(self, other)
    """

    """
    Comparision Operator:
    <	__lt__(self, other)
    >	__gt__(self, other)
    <=	__le__(self, other)
    >=	__ge__(self, other)
    ==	__eq__(self, other)
    !=	__ne__(self, other)
    """

    """
    Assignment Operators:
    -=	__isub__(self, other)
    +=	__iadd__(self, other)
    *=	__imul__(self, other)
    /=	__idiv__(self, other)
    //=	__ifloordiv__(self, other)
    %=	__imod__(self, other)
    **=	__ipow__(self, other)
    >>=	__irshift__(self, other)
    <<=	__ilshift__(self, other)
    &=	__iand__(self, other)
    |=	__ior__(self, other)
    ^=	__ixor__(self, other)
    """

    """
    Unary Operators:
    –	__neg__(self)
    +	__pos__(self)
    ~	__invert__(self)
    """

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __gt__(self, other) -> bool:
        return True if self.age > other.age else False


roger = Dog("Roger", 8)
bob = Dog("Syd", 10)
if roger > bob:
    print(f"{roger.name} is older than {bob.name}")
else:
    print(f"{roger.name} is less or equal to {bob.name}")
