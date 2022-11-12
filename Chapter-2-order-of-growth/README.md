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


