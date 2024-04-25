print('Hello World')

import math

def square_root(num):
    return math.sqrt(num)

def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-1])
    return fib_seq

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is:", factorial(num))
    fibnum = int(input("Enter a number: "))
    fib_seq = fibonacci(fibnum)
    print("Fibonacci sequence up to", num, "is:", fib_seq)