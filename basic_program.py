print('Hello World')

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is:", factorial(num))
    number = int(input("Enter the value of n: "))
    print("The", number, "th prime number is:", nth_prime(number))
