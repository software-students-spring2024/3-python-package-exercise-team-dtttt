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

