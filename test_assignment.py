import pytest
import inspect
from assignment import (
    product_of_digits,
    sum_even_or_odd,
    contains_five,
    sum_even_digits
)

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source


# ---------------------------
# Exercise 1: Product of digits
# ---------------------------
@pytest.mark.parametrize("num, expected", [
    (234, 24),
    (105, 0),
    (7, 7),
    (999, 729),
    (5012, 0)
])
def test1(num, expected):
    assert product_of_digits(num) == expected
    assert check_contains_loop(product_of_digits)


# ---------------------------
# Exercise 2: Sum of digits (even or odd)
# ---------------------------
@pytest.mark.parametrize("num, expected", [
    (1234, "Even"),
    (246, "Even"),
    (135, "Odd"),
    (1001, "Even"),
    (9, "Odd")
])
def test2(num, expected):
    assert sum_even_or_odd(num) == expected
    assert check_contains_loop(sum_even_or_odd)


# ---------------------------
# Exercise 3: Contains digit 5
# ---------------------------
@pytest.mark.parametrize("num, expected", [
    (1542, True),
    (9087, False),
    (5, True),
    (123456789, True),
    (4004, False)
])
def test3(num, expected):
    assert contains_five(num) == expected
    assert check_contains_loop(contains_five)


# ---------------------------
# Exercise 4: Sum of even digits
# ---------------------------
@pytest.mark.parametrize("num, expected", [
    (48273, 14),
    (13579, 0),
    (0, 0),
    (2222, 8),
    (9081726354, 20)   # even digits: 0+8+2+6+4 = 20
])
def test4(num, expected):
    assert sum_even_digits(num) == expected
    assert check_contains_loop(sum_even_digits)
