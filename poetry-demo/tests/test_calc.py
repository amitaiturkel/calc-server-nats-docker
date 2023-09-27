import pytest
from poetry_demo.calc_server import Calc

@pytest.fixture
def calculator():
    return Calc()

def test_add(calculator):
    calculator.add(5)
    assert calculator.result == 5

    calculator.add(-3)
    assert calculator.result == 2

def test_subtract(calculator):
    calculator.subtract(3)
    assert calculator.result == -3

    calculator.subtract(-2)
    assert calculator.result == -1

def test_multiply(calculator):
    calculator.multiply(4)
    assert calculator.result == 0

    calculator.add(2)
    calculator.multiply(3)
    assert calculator.result == 6

def test_divide(calculator):
    calculator.divide(2)
    assert calculator.result == 0

    calculator.add(10)
    calculator.divide(5)
    assert calculator.result == 2.0

def test_divide_by_zero(calculator):
    calculator.divide(0)
    # If you want to add a print statement for the caught exception:

def test_clear(calculator):
    calculator.add(8)
    calculator.clear()
    assert calculator.result == 0

def test_multiple_operations(calculator):
    calculator.add(5)
    calculator.subtract(2)
    calculator.multiply(3)
    calculator.divide(3)
    assert calculator.result == 3.0

