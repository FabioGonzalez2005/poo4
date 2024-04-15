import pytest

def divide(a:int, b:int):
    if (b == 0):
        raise ValueError("Cannot divide by zero")

def test_exception():
    a = 0
    b = 10
    with pytest.raises(ZeroDivisionError):
        b / a

def test_divide():
    with pytest.raises(ValueError) as exception_info:
        divide(10,0)
    assert str(exception_info.value).lower == "cannot divide by Zero".lower