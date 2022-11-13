# Order of Growth
- This has some limitation for example if n >= 999 then the order of growth of f(n) > order of growth of g(n).  
- Practically, we may never reach that large number. Therefore, Order of Growth has certain limitation.

# How Order of Growth measures algorithm ?
- Order of growth is used for theoritical analysis of algorithm.  
- When Order of Growth of the function, which represents the time taken by the algorithm, is higher than that of other algorithm, then that algorithm is considered a Bad Algorithm.
- A function f(n) is said to be growing faster than g(n) if
- $lim_{n\to\infty} f(n)/g(n) = ∞ $  
- $lim_{n\to\infty} g(n)/f(n) = 0 $  
- This is based on assumption that n >= 0, Time Taken >= 0 and f(n), g(n) >=0   
- Let us do some computing to find out it theoritically.
- Let $f(n) = n^2 + n + 6$
- And $g(n) = 2n + 5$

![image3](https://user-images.githubusercontent.com/74963600/201471469-e79e7cf3-df59-4233-9b1c-c0cea474ea8d.jpg)
- So, we could see that theoritically we can prove $lim_{n\to\infty} g(n)/f(n) = 0 $  is true.
- Therefore, f(n) is growing faster than g(n)

# How to determine which order of growth is lower or faster.
- 1. Ignore lower order terms
- 2. Ignore leading constants
- 3. And then by using below info decide which one is of lower order 
![image4](https://user-images.githubusercontent.com/74963600/201471474-b7f27486-993b-4763-9800-705a2bbc81ad.jpg)
- **The functions that will have lower order will have lower order of growth and so the faster in execution**
- We can test our understanding using below examples  
![image5](https://user-images.githubusercontent.com/74963600/201471490-4a578306-8aa3-4ffb-95f6-c8a232aa5f32.jpg)
- In the above example, $n < n^2$ - therefore, g(n) has lower order of growth than f(n) and hence it executes faster than f(n)  
![image6](https://user-images.githubusercontent.com/74963600/201471493-16f0e7a8-4179-4677-82a2-c76f710d5f02.jpg)
- In the above example, $log(n) < n$ - therefore, f(n) has lower order of growth than g(n) and hence it executes faster than g(n)  
![image7](https://user-images.githubusercontent.com/74963600/201471503-eea1fe1a-beaf-41c4-a4ac-454cbbd22f3c.jpg)  
- In the above example, $n^2 > n*log(n)$ - therefore, g(n) has lower order of growth than f(n) and hence it executes faster than f(n)  
