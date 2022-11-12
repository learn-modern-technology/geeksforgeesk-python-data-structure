"""
What is Asymptotic analysis

Time taken to execute a program depends on various factors
1. Machine on which the program runs.
2. Depends on the programming language
3. Loads on the machine where the program is running
So, it is not possible to determine which program runs faster
So, we have theoritical solutions to determine which programs run faster
This is called asymptotic analysis

"""

"""
Asymptotic Analysis - is a theoritical analysis. 
It is not dependent on any machine, programming language etc.
We don't hve to implement all ideas or algorithm

Asymptotic analysis is all about measuring order of growth in terms of input size
"""

""" 
For the sum-of-numbers-upto-n.py program 
Order of growth of fn - sum_of_numbers_till_n   - C1 (Constant)
Order of growth of fn - sum_till_n_numbers      - C2*n + C3
Order of growth of fn - sum_till_n_for          - C2*n + C3
Order of growth of fn - sum_till_n_double_loop  - C4 (n)^2 + C5 n + C6
"""

""" 
For function sum_of_numbers_till_n - we have used formula.
So, the order of growth is constant - C1.
Because for every number n the program does - 1 addition, 1 multiplication and 1 division.
And we assume that both 100x100 and 10000x10000 will take same time.
And each operation we are doing only once not n times. So, we have Fixed number of operations.
There for Order of growth is Constanct C1
"""

""" 
For function sum_till_n_numbers and  sum_till_n_for - we don't have formula.
We have some Initialization, some loop till n time, we have some operations that runs in a loop
So, the order of Growth is - C2n
Then we have some constant operation as well, so order of growth is - C3
"""

""" 
For function sum_till_n_double_loop-
we have 2 loops, one addition and initialization
And the loop will execute n*(n+1)/2 times, which is equal to (n)^2 + n 
There for cost of growth of this function is - C4 (n)^2 + C5 n + C6
"""

""" 
If we plot these Cost of growth on the X-Y Axis (1st Quadrant), then we will understand - 
the greater the number used in the fucntion, the higher cost of growth for fucntions that will use complex logics.
"""
![image1](https://user-images.githubusercontent.com/74963600/201460754-23588c0b-4e43-49ab-9eee-8e67a5ae53fc.png)

""" 
Let us say the cost of growth of first function is f(n) and the cost of growth of second function is g(n)
f(n) - 
"""

