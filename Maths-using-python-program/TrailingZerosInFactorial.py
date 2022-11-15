def calculate_factorial(num):
    if num == 0:
        return 1
    while num > 0:
        return num * calculate_factorial(num-1)
    
def trailing_zeros_in_factorial(num):
    count_zero = 0
    temp = num
    while num > 5:
        num //= 5
        count_zero += num
    
    return count_zero 

if __name__ == "__main__":
    number = 100
    print(f"{number}! is {calculate_factorial(number)}")
    print(f"Trailing Zeros in- {number}! is {trailing_zeros_in_factorial(number)}")
   

    