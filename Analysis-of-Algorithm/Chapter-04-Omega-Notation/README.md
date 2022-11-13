# Ω - Omega Notation (Lower Limit on Order of Growth)

# **How to calculate Ω Notation of $f(n)$**
- Let us take a example  
  - 1. $f(n) = 3n^2 + 2n + 100$
    - Ignore leading constants - the number 3
    - Ignore lower order terms - $2n$ and $100$
    - We are left with $n^2$
    - We can say that $f(n)=Ω(n^2)$

  - 2. $f(n) = 4n + logn + 30$
    - Ignore leading constants - the number 4
    - Ignore lower order terms - $logn$ and $30$
    - We are left with $n$
    - We can say that $f(n)=Ω(n)$  

# ** Mathematical Definition of Ω Notation 
- We can say $f(n) = Ωg(n)$ if there exist constants c and $n_0$ such that  
  $0<=cg(n)<=f(n)$ for all $n >= n_0$
- This mathematical definition can be useful to proove that Omega notation that we found is correct.
- Example:  
  $f(n)=2n+3$ can be written as Ω(n). It implies that g(n)=n
- Let us try to see how we can proove or verify that Omega notation that we found is correct  
  - 1. $0<=cg(n)<=f(n)$ for all $n >= n_0$
    -  $0<=cn<=2n+3$ for all $n >= n_0$
    -  For solving purpose, we will take c as the previous value of the highest growing term. 
    -  In this case, the highest growing term is $2n$. 
    -  So, previous value is - $c=1$
    -  So, $cg(n)=n$
    -  Now, we have to find $n_0$  
    -  It implies $n<=2n+3$. So, $0<=n$. This implies, n_0 = 0
    -  So, when n >= 0, the f(n) is always greater.

- Some more example of Omega Notation - Please see the examples below
![image10](https://user-images.githubusercontent.com/74963600/201490556-5bb249a3-15ea-4020-8bdf-59858f20d17f.jpg)

![image11](https://user-images.githubusercontent.com/74963600/201490558-ffac0001-873c-4427-a728-f043be82d43d.jpg)
