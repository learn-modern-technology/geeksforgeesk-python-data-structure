def isPalindrome(num):
    temp = num
    sum = 0
    while(num > 0):
        rem = num % 10
        num = int(num / 10)
        sum = sum * 10 + rem
    
    return sum == temp

if __name__ == '__main__':
    n = 15351
    print(f"The number {n} is a Palindrome ? - {isPalindrome(n)}")