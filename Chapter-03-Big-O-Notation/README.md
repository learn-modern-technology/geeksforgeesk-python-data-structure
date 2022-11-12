# Big O Notation (Upper Limit on Order of Growth)

# **How to calculate Big O Notation of $f(n)$**
- Let us take a example  
  - 1. $f(n) = 3n^2 + 2n + 100$
    - Ignore leading constants - the number 3
    - Ignore lower order terms - $2n$ and $100$
    - We are left with $n^2$
    - We can say that $f(n)=O(n^2)$

  - 2. $f(n) = 4n + logn + 30$
    - Ignore leading constants - the number 4
    - Ignore lower order terms - $logn$ and $30$
    - We are left with $n$
    - We can say that $f(n)=O(n)$  

# ** Mathematical Definition of Big O Notation 
- We can say $f(n) = Og(n)$ if there exist constants c and $n_0$ such that  
  $f(n)<=cg(n)$ for all $n >= n_0$
- This mathematical definition can be useful to proove that Big O notation that we found is correct.
- Example:  
  $f(n)=2n+3$ can be written as O(n). It implies that g(n)=n
- Let us try to see how we can proove or verify that Big O notation that we found is correct  
  - 1. $f(n)<=cg(n)$ for all $n >= n_0$
    -  $2n+3<=cn$ for all $n >= n_0$
    -  For solving purpose, we will take c as the next value of the highest growing term. 
    -  In this case, the highest growing term is $2n$. 
    -  So, next value is - $c=3$
    -  Now, we have to find $n_0$  
    -  It implies $(2n+3) <= 3n$. So, $3<=n$. This implies, n_0 = 3
    -  So, when n >= 3, the f(n) is always greater.

- Some more example of Big O Notation - Please see the examples below