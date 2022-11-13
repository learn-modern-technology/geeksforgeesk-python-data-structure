# Space Complexity
## It is very similar to Time Complexity analysis. 
- In time complexity, we talk about order of growth of time taken in terms of Input Size.
- In Space Complexity, we talk about order of growth of Memory (on RAM) usage in terms of input.

# Auxillary Space:  
- Auxillary space tells us order of growth of extra spaces( spaces other than input/output)

### Example 1:
    
    ```Python
    def sum_of_numbers_n(num):
        sum = (num/2) * (num+1)
        return sum
    ```
    - The above example takes constant space. So, space complexity is denoted by $θ(1)$ or $O(1)$

### Example 2:

    ```Python
    def getSum2(n):
        sum = 0
        i = 1
        while i < n:
            sum = sum + i
            i = i + 1
        return sum
    ```
    - The above example takes constant space beacuse all variables are constant variables.
    - So, space complexity for this function is denoted by $θ(1)$ or $O(1)$

### Example 3:

    ```Python
    def listSum(l):
        sum = 0
        for x in l:
            sum = sum + x
        return sum
    ```
    - Space taken by this function depends on the size of the list.
    - So, space complexity for this function is denoted by $θ(n)$.
    - Auxillary space - required here is constant. Because space needed for storing the object valuesare all constant.

### How to calculate Space or Auxill!ary Complexity

![image17](https://user-images.githubusercontent.com/74963600/201538210-9ef33e2e-5f51-47ea-8fa4-13ae5254e9a8.jpg)

