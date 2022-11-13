# **Analysis of Common Loops**  

## First Example of Loops (Determine the order of growth)  
- Example 1:
    ```Python
    i = 0
    while i < n:
        i = i + c
        ## Some other constant
        ## Time work
    ```
    - If n = 10 and c = 2. So, the loop will execute for n = 0,2,4,6,8
    - If n = 11 and c = 2. So, the loop will execute for n = 0,2,4,6,8,10
    - In general we can say that the loop run $[n/c]$ times.
    - Since, we can ignore constant. we can say order of growth of For Loop is θ(n)
    - The equivalent for loop will also have same cost of growth - θ(n)
 
- Example 2:
    ```Python
    i = n
    while i > 0:
        i = i - c
        ## Some other constant
        ## Time work
    ```
    - If n=10 and c=2, the loop will execute for 11,9,7,5,3,1
    - In general we can say that the loop run $[n/c]$ times.
    - Since, we can ignore constant. we can say order of growth of For Loop is θ(n)

- Example 3:
    ```Python
    i = 1
    while i < n:
        i = i * c
        ## Some other constant
        ## Time work
    ```
    - If n=32 and c=2, the loop will execute for 1,2,4,8,16
    - If n=33 and c=2, the loop will execute for 1,2,4,8,16,32
    - The loop runs in sequence - $2^0$, $2^1$, $2^2$, $2^3$, $2^4$..... $2^(k-1)$
    - $c^(k-1) <n $
    - $k-1=log n / log c $
    - $k=log n+1$
    - Since, we can ignore constant. we can say order of growth of For Loop is θ(log n)
    - The equivalent for loop will also have same cost of growth - θ(log n)

- Example 4:
    ```Python
    i = 1
    while i < n:
        i = i / c
        ## Some other constant
        ## Time work
    ```
    - If n=32 and c=2, the loop will execute for 32, 16, 8, 4, 2
    - If n=33 and c=2, the loop will execute for 33, 16, 8, 4, 2
    - This is very similar to previous example.
    - So order of cost of growth - θ(log n)

- Example 5:
    ```Python
    i = 2
    while i < n:
        i = i**c
        ## Some other constant
        ## Time work
    ```
    - If n=32 and c=2, the loop will execute for 2, 4, 16
    - The loop runs in sequence - $2^1$, $2^2$, $2^2^2$....... $2^c^(k-1)$
    - $2^c^(k-1) <n $
    - $c^(k-1) < log n $
    - $k < log(log n) + 1 $
    - Since, we can ignore constant. we can say order of growth of For Loop is θ(log(log n))
    - The equivalent for loop will also have same cost of growth - θ(log(log n))
    - So order of cost of growth - θ(log(log n))

- Example 6:
    ```Python
    i = 0
    while i < n:
        i = i + 2
        ## Some other constant
        ## Time work

    i = 1
    while i < n:
        i = i * 3
        ## Some other constant

    i = 1
    while i < 100:
        i = i + 1
        ## Some other constant
    ```
    - Cost of Order for 1st while loop is - θ(n)
    - Cost of Order for 2nd while loop is - θ(log n)
    - Cost of Order for 3rd while loop is - θ(1)
    - Overall Code Order group is -  θ(n) + θ(log n) + θ(1)
    - Ignoring lower order term  - Order of Code is θ(n)

- Example 7: Nested While Loop
    ```Python
    i = 0
    while i < n:
        j = 1
        while j < n:
            j = j * 2
        i = i + 1
        ## Some other constant
    ```
    - Order of growth of Inner While Loop is θ(log n)
    - Order of growth of Outer While loop is θ(n)
    - For every outer loop execution, inner loop will run. So we will multiply the inner loop cost of growth as well.
    - So, the time complexity of the code is θ(n) * θ(log n) = θ(nlog n)

- Example 8: Subsequent Nested While Loop
    ```Python
    i = 0
    while i < n:
        j = 1
        while j < n:
            j = j * 2
        i = i + 1
        ## Some other constant
    
    i = 0
    while i < n:
        j = 1
        while j < n:
            j = j + 1
        i = i + 1
        ## Some other constant
    ```
    - Order of growth of 1st while Loop is  θ(n) * θ(log n) = θ(nlog n)
    - Order of growth of 2nd while loop is θ(n) * θ(n) = θ($n^2$)
    - For every outer loop execution, inner loop will run. So we will multiply the inner loop cost of growth as well.
    - So, the time complexity of the code is θ($n^2$) + θ(nlog n) = θ($n^2$).

- Example 9: Subsequent Nested While Loop with multiple input
    ```Python
    i = 0
    while i < n:
        j = 1
        while j < n:
            j = j * 2
        i = i + 1
        ## Some other constant
    
    i = 0
    while i < m:
        j = 1
        while j < m:
            j = j + 1
        i = i + 1
        ## Some other constant
    ```
    - Order of growth of 1st while Loop is  θ(n) * θ(log n) = θ(nlog n)
    - Order of growth of 2nd while loop is θ(n) * θ(n) = θ($m^2$)
    - For every outer loop execution, inner loop will run. So we will multiply the inner loop cost of growth as well.
    - So, the time complexity of the code is θ($m^2$) + θ(nlog n)