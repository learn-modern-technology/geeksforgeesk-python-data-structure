# **Analysis of Recusive Function**
- Recurrence relation for the time taken by the function.
- When we want to find out the Time complexity of the recursive code  
  we write recurrence relation for the time taken by the function and then we solve this recursive relation.

## Examples to Find Recursive Relation
- Example 1:
    ```Python
    def fun(n):
        if n==1:
            return
        for i in range(n):
            print('GfG')
        fun(n/2)
        fun(n/2)
    ```
    - In the program above, it is making 2 recursive function call.
    - This recursive function will take T(n/2). So, total is 2T(n/2)
    - For loop will run n times. So, it will take θ(n).
    - So, $T(n) = 2T(n/2) + θ(n)$
    - For other cases when n is 1. $T(1)= θ(1)$
    - Recurrence Relation is given by expression
        - $T(n) = 2T(n/2) + θ(n)$
        - $T(1)= θ(1)$
    
- Example 2:
    ```Python
    def fun(n):
        if n==1:
            return
        print('GfG')
        fun(n/2)
        fun(n/2)
    ```
    - In the program above, it is making 2 recursive function call.
    - This recursive function will take T(n/2). So, total is 2T(n/2)
    - For print statement, it will take θ(1).
    - So, $T(n) = 2T(n/2) + θ(1)$
    - For other cases when n is 1. $T(1)= θ(1)$
    - Recurrence Relation is given by expression
        - $T(n) = 2T(n/2) + θ(1)$
        - $T(1)= θ(1)$

- Example 3:
    ```Python
    def fun(n):
        if n==1:
            return
        print(n)
        fun(n-1)
    ```
    - In the program above, it is making 1 recursive function call.
    - This recursive function will take T(n-1). So, total is T(n-1) for n>1
    - For print statement, it will take θ(1).
    - So, $T(n) = T(n-1) + θ(1)$  for all n>1
    - For other cases when n is 1. $T(1)= θ(1)$
    - Recurrence Relation is given by expression
        - $T(n) = 2T(n-1) + θ(1)$
        - $T(1)= θ(1)$

## **Analysis of Recursion**
- We will use Recursion Tree Method to perform analysis.
    ### ** Recursion Tree Method **
    - We write non-recursive part as root of tree and recursive parts as children
    - We keep expanding children until we see a pattern
    - We need to divide the tree into 2 parts:-
        - $T(n) = 2T(n/2) + θ(n)$
        - $T(1)= θ(1)$
        - Recursion Tree:- 2T(n/2)
        - Non Recursion Tree:- θ(n)    
    - Let Cn = θ(n)  
    - At each level of recursion tree- I will do Cn amount of work.
    - The target of the recursion tree is to find out the amount of work done.
    - We need to add Cn the no of times the height of the tree.
    - Total work done = Cn + Cn + Cn + ........ upto log(n)  times
    - Total work done - Cn*log(n)
    - Overall Time Complexity is $θ(nlog(n))$

    - For expression:
        - $T(n) = 2T(n-1) + θ(1)$
        - $T(1)= θ(1)$
    - Let Cn = θ(n)  
    - At 1st level of recursion tree- I will do C amount of work.
    - At 2nd level of recursion tree- I will do 2C amount of work.
    - At 3rd level of recursion tree- I will do 4C amount of work and so on.
    - The target of the recursion tree is to find out the amount of work done.
    - We need to add C the no of times the height of the tree.
    - Total work done = C + 2C + 4C + ........ 2^nC
    - Total work done - $θ(2^n)$
    - Overall Time Complexity is $θ(2^n)$

    - For expression:
        - $T(n) = T(n/2) + θ(1)$
        - $T(1)= θ(1)$
    - Let Cn = θ(n)  
    - At 1st level of recursion tree- I will do C amount of work.
    - At 2nd level of recursion tree- I will do C amount of work.
    - At 3rd level of recursion tree- I will do C amount of work and so on.
    - The target of the recursion tree is to find out the amount of work done.
    - We need to add C the no of times the height of the tree.
    - Total work done = C + C + C + ........ C
    - Total work done - $θ(logn)$
    - Overall Time Complexity is $θ(logn)$

    - For expression:
        - $T(n) = 2T(n/2) + θ(1)$
        - $T(1)= θ(1)$
    - Let Cn = θ(n)  
    - At 1st level of recursion tree- I will do C amount of work.
    - At 2nd level of recursion tree- I will do 2C amount of work.
    - At 3rd level of recursion tree- I will do 4C amount of work and so on.
    - The target of the recursion tree is to find out the amount of work done.
    - We need to add C the no of times the height of the tree.
    - Total work done = C + 2C + 4C + ........
    - Total work done - $θ(n)$
    - Overall Time Complexity is $θ(n)$

    - Some other examples for Analysing the Time Complexity  
    
    ![image14](https://user-images.githubusercontent.com/74963600/201532227-f49098a0-c152-4dad-acb6-8da8196c664a.jpg)
    
    ![image15](https://user-images.githubusercontent.com/74963600/201532240-75ba272e-0b8d-4611-be8c-89dfb4904f29.jpg)
    
    ![image16](https://user-images.githubusercontent.com/74963600/201532256-5194137d-0cad-453d-9350-0f5fe7760d7b.jpg)
