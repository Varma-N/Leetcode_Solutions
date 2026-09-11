# Problem 1979: Find Greatest Common Divisor of Array

## Intuition
The solution leverages the properties of the Greatest Common Divisor (GCD) problem, where the GCD of two numbers can be determined by repeatedly finding the remainder of one number divided by the other. In this case, we can find the GCD by finding the remainder of the smallest number and the largest number in the array. 

## Approach
1. **Sort the array:** The input array `nums` is first sorted in ascending order.
2. **Initialization:** The smallest number (`small_num`) and the largest number (`large_num`) are initialized as the first and last elements of the sorted array, respectively.
3. **Iterative process:** We use a `while` loop that continues as long as `large_num` is not zero.
   - **Remainder:** Inside the loop, `small_num` is updated to be the value of `large_num`, and `large_num` is updated to be the remainder of the division of `large_num` by `small_num` (`large_num % small_num`).
4. **Return:** The final `small_num` represents the GCD.


## Complexity Analysis
* **Time Complexity:** $O(N \log N)$
    * Sorting the array in ascending order takes $O(N \log N)$ time.
    * The `while` loop iterates at most $N$ times. 
* **Space Complexity:** $O(1)$
    * We only use constant extra space to store the variables, so the space complexity is $O(1)$.