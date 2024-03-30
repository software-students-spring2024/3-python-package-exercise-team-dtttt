
from calc import add, subtract, multiply, divide, mod, stringParse, log, exp, abs, factorial, mean, median, mode, randomnumsrange, cubesurfacearea

def main():
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication: 5 * 3 =", multiply(5, 3))
    print("Division: 5 / 2 =", divide(5, 2))
    print("Modulo: 5 mod 2 =", mod(5, 2))
    
    print("String Parsing: '10 + 5' =", stringParse("10 + 5"))
    print("Logarithm: log(100, 10) =", log(100, 10))
    print("Exponentiation: 2 ^ 3 =", exp(2, 3))
    print("Absolute Value: abs(-5) =", abs(-5))
    print("Factorial: 5! =", factorial(5))
    
    sample_list = [1, 2, 3, 4, 5, 6]
    print("Mean: ", mean(sample_list))
    print("Median: ", median(sample_list))
    print("Mode: ", mode([1, 2, 2, 3, 4]))
    print("Random Numbers Range: 0 to 10, 5 times =", randomnumsrange(10, 5))
    print("Cube Surface Area: Side length 3 =", cubesurfacearea(3))
    
if __name__ == "__main__":
    main()
