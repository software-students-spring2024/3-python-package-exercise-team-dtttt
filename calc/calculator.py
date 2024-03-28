import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def mod(x, y):
    if y == 0:
        raise ValueError("Cannot mod by zero.")
    return x % y
def stringParse(input):
    # no  parentheses, operator precedence, or numbers without spaces around the operators
    parts = input.split()

    if len(parts) != 3:
        raise ValueError("Input should be in the format: 'number1 operation number2'")

    xTr, operator, yTr = parts
    x = float(xTr)
    y = float(yTr)

    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)
    elif operator.lower() == 'mod':
        return mod(x, y)
    else:
        raise ValueError(f"Unsupported operation: {operator}")

def log(x,y):
    # value x, base y, works only for int results
    if y == 1 or x <= 0 or y <= 0:
        raise ValueError("x, y must be positive, y shouldn't be 1")
    return round(math.log(x,y))

def exp(x, y):
    if y < 0:
        x = 1/x
        y = -y
    res = 1
    for i in range(y):
        res *= x
    return res

def abs(x):
    if x < 0:
        x = -x
    return x

def factorial(x, val = {}):
    if x < 0:
        raise ValueError("x must be positive")
    if x in val:
        return val[x]
    if x == 0:
        val[x] = 1
        return 1
    val[x] = x*factorial(x-1, val)
    return val[x]