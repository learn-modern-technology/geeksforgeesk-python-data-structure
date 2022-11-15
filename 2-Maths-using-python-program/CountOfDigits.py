def count_of_digits(number):
    count = 0
    while(number > 0):
        number //=10
        count += 1
    
    return count

if __name__ == '__main__':
    n = 156893
    print(f"No. of digits of {n} are - {count_of_digits(n)}")