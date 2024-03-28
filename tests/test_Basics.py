import pytest
from calc import add, subtract, multiply, divide, mod, stringParse, log, exp, abs, factorial


def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(10, 5) == 2
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    with pytest.raises(ValueError):
        divide(10, 0)

def test_mod():
    assert mod(10, 3) == 1, "C: 1"
    assert mod(10, 10) == 0, "C: 0"
    assert mod(0, 10) == 0, "C: 0"
    assert mod(-10, 3) == 2, "C: 2"
    with pytest.raises(ValueError):
        mod(10, 0), "Should raise ValueError for division by zero"

def test_stringParse_addition():
    assert stringParse("10 + 5") == 15, "C: 15"

def test_stringParse_subtraction():
    assert stringParse("10 - 5") == 5, "C: 5"

def test_stringParse_multiplication():
    assert stringParse("10 * 5") == 50, "C: 50"

def test_stringParse_division():
    assert stringParse("10 / 2") == 5, "C: 5"
    with pytest.raises(ValueError):
        stringParse("10 / 0"), "C: raise ValueError for division by zero"

def test_stringParse_mod():
    assert stringParse("10 mod 3") == 1, "C: 1"
    with pytest.raises(ValueError):
        stringParse("10 mod 0"), "C: raise ValueError for mod by zero"

def test_stringParse_invalid_input():
    with pytest.raises(ValueError):
        stringParse("10"), "C: raise ValueError for invalid input format"
    with pytest.raises(ValueError):
        stringParse("10 ^ 2"), "C: raise ValueError for unsupported operation"
    with pytest.raises(ValueError):
        stringParse("one + two"), "C: raise ValueError for non-numeric input"

def test_log():
    assert log(10, 10) == 1
    assert log(100, 10) == 2
    assert log(1000, 10) == 3
    assert log(64, 2) == 6
    with pytest.raises(ValueError):
        log(-1,10), "Should raise ValueError"

def test_exp():
    assert exp(2, 3) == 8
    assert exp(1, 10) == 1
    assert exp(4, -1) == 0.25 

def test_abs():
    assert abs(0) == 0
    assert abs(-2) == 2
    assert abs(3) == 3

def test_factorial():
    assert factorial(0) == 1
    assert factorial(3) == 6
    assert factorial(10) == 3628800
    with pytest.raises(ValueError):
        factorial(-4), "Should raise ValueError"