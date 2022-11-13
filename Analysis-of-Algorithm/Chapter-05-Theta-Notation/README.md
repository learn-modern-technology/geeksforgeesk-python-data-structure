# θ - Theta Notation (Exact Limit on Order of Growth)
- It actually represents an exact bounds on the Order of Growth of the Function

# **How to calculate θ Notation of $f(n)$**
- Let us take a example  
  - 1. $f(n) = 3n^2 + 2n + 100$
    - Ignore leading constants - the number 3
    - Ignore lower order terms - $2n$ and $100$
    - We are left with $n^2$
    - We can say that $f(n)=θ(n^2)$

  - 2. $f(n) = 4n + logn + 30$
    - Ignore leading constants - the number 4
    - Ignore lower order terms - $logn$ and $30$
    - We are left with $n$
    - We can say that $f(n)=θ(n)$  

# ** Mathematical Definition of θ Notation 
- We can say $f(n) = θg(n)$ if there exist constants $c_1$, $c_2$ and $n_0$ such that    
  $0<=c_1 g(n)<=f(n)<=c_2 g(n)$ for all $n >= n_0$
- This mathematical definition can be useful to proove that Omega notation that we found is correct.
- Example:  
  $f(n)=2n+3$ can be written as θ(n). It implies that g(n)=n
- Let us try to see how we can proove or verify that Omega notation that we found is correct  
  - 1. $0<=c_1 g(n)<=f(n)<=c_2 g(n)$ for all $n >= n_0$
    -  For solving purpose, we will take $c_1$ as the previous value of the highest growing term.
    -  For solving purpose, we will take $c_2$ as the next value of the highest growing term. 
    -  In this case, the highest growing term is $2n$. 
    -  So, previous value is - $c_1=1$
    -  So, next value is - $c_2=3$
    -  And, $cg(n)=n$
    -  $c_1n<=2n+3$ for all $n >= n_0$
    -  $n>-3$. But $n$ can't be less than zero. Therefore, $n>=0$ is one of the range
    -  $2n+3<3n$ for all $n >= n_0$
    -  Therefore, $n>3$ is the upper range.
    -  Now, we have to find $n_0$  
    -  This implies, n_0 = 3
    -  So, when n >= 3, the f(n) is always greater.

# Theta Notation is useful when we know the exact bound.
- Ideally, we should use the Theta notation wherever we know the exact bound.
- For example - Time complexity to find Max, Min and Average in an array can be represneted using Theta Notation

- Some more example of Theta Notation - Please see the examples below
