def factorial_of_number(n):
    if n == 0:
        return 1
    
    while(n > 0):
        return n * factorial_of_number(n-1)

if __name__ == "__main__":
    num = 10
    print(f"Factorial of number - {num} is {factorial_of_number(num)}")