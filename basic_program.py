print('Hello World')

import math

def square_root(num):
    return math.sqrt(num)

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    print("Square root of", num, "is:", square_root(num))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is:", factorial(num))
