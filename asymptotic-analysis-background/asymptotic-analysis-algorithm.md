
# What is Asymptotic analysis

## Time taken to execute a program depends on various factors
- Machine on which the program runs.
- Depends on the programming language
- Loads on the machine where the program is running
- Therefore, it is not possible to determine which program runs faster
- So, we have theoritical solutions to determine which programs run faster
- This method is called asymptotic analysis

## Asymptotic Analysis - 
- ** Asymptotic analysis is all about measuring order of growth in terms of input size.
- ** It is a theoritical analysis. 
- ** It is not dependent on any machine, programming language etc. 
- ** We don't hve to implement all ideas or algorithm.

 
## For the sum-of-numbers-upto-n.py program 
- ** Order of growth of f(n) - sum_of_numbers_till_n   - C1 (Constant)
- ** Order of growth of g(n) - sum_till_n_numbers      - C2*n + C3
- ** Order of growth of g(n) - sum_till_n_for          - C2*n + C3
- ** Order of growth of h(n) - sum_till_n_double_loop  - C4 (n)^2 + C5 n + C6

## For function sum_of_numbers_till_n 
- ** we have used formula.
- ** So, the order of growth is constant - C1.
- ** Because for every number n the program does - 1 addition, 1 multiplication and 1 division.
- ** And we assume that both 100x100 and 10000x10000 will take same time.
- ** And each operation we are doing only once not n times. So, we have Fixed number of operations.
- ** Therefore Order of growth is Constanct C1

## For function sum_till_n_numbers and  sum_till_n_for - we don't have formula.
- ** We have some Initialization, some loop till n time, we have some operations that runs in a loop
- ** So, the order of Growth is - C2n
- ** Then we have some constant operation as well, so order of growth is - C3
 
## For function sum_till_n_double_loop-
- ** We have 2 loops, one addition and initialization
- ** And the loop will execute n*(n+1)/2 times, which is equal to (n)^2 + n 
- ** There for cost of growth of this function is - C4 (n)^2 + C5 n + C6

## Let us compare or analyze the function to determine the best function
- If we plot these Cost of growth on the X-Y Axis (1st Quadrant), then we will understand - 
the greater the number used in the fucntion, the higher the cost of growth for fucntions that will use complex logics.

- Let us say the cost of growth of first function is f(n) and the cost of growth of second function is g(n)
- Then the f(n) will will perform evenly through out, but the time taken for g(n) will keep increasing. 
- Initially, time taken for g(n) will be less than f(n) but after a certain limit, it will take more time than f(n)

![image1]https://github.com/learn-modern-technology/geeksforgeesk-python-data-structure/blob/b835d99768a48260fa573d779bc6f1a9a3e38222/asymptotic-analysis-background/image1.jpg?raw=true

![image2]https://github.com/learn-modern-technology/geeksforgeesk-python-data-structure/blob/develop/asymptotic-analysis-background/image2.jpg






