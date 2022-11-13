## To find the sum of n consecutive numbers
import os

def sum_of_numbers_till_n(num):
    sum = (num/2) * (num+1)
    return sum

def sum_till_n_numbers(num):
     sum = 0
     while num > 0:
         sum = sum + num
         num = num - 1
     return sum

def sum_till_n_for(num):
    sum = 0
    for x in range(1, num+1):
        sum = sum + x
    return sum

def sum_till_n_double_loop(num):
    sum = 0
    for i in range(1, num+1):
        for x in range(1,i+1):
            sum = sum + 1
    return sum

input_val = int(input("Enter the n for which sum upto n should be caluclated -"))
print('sum_of_numbers_till_n - ',sum_of_numbers_till_n(input_val))
print('sum_till_n_numbers - ',sum_till_n_numbers(input_val))
print('sum_till_n_numbers - ',sum_till_n_for(input_val))
print('sum_till_n_double_loop - ',sum_till_n_double_loop(input_val))