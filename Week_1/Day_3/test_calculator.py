
import pytest
from calculator import add, subtract, multiply, divide

# An example of using fixtures to provide test data
# @pytest.fixture
# def numbers():
#     return 2, 3  # a = 2, b = 3

#Test add function
def test_add_two_numbers():
    result = add(2, 3)
    assert result == 5

#Test subtract function
def test_subtract_two_numbers():
    result = subtract(5, 3)
    assert result == 2

#Test multiply function
def test_multiply_two_numbers():
    result = multiply(4, 3)
    assert result == 12

#Test divide function
def test_divide_two_numbers():
    result = divide(10, 2)
    assert result == 5

#Test divide by zero
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)