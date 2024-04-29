import pytest

def divide(a:int, b:int):
    if (b == 0):
        raise ValueError("Cannot divide by zero")

def test_exception():
    a = 0
    b = 10
    with pytest.raises(ZeroDivisionError):
        b / a