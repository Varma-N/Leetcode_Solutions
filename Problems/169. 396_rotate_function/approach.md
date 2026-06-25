# Problem 396: Rotate Function

## Intuition
The core idea is to calculate the sum of products based on rotation positions.  We can achieve this by iteratively calculating the rotation sums for each position and keeping track of the maximum value. 

## Approach
1. **Initialization:** 
   - Calculate `n` which is the length of the input array.
   - Determine the total sum of elements in the array: `s = sum(nums)`.
2. **Calculating Initial Sum of Products (f):**  
    - Calculate the initial sum of products using a formula based on rotations and element indices: `f = sum(i * val for i, val in enumerate(nums))`
3. **Iterative Calculation:** 
   - Iterate through the input array in reverse order (`reversed(nums)`).
   - For each iteration:  
     - Calculate the new product sum based on the current rotation position by taking `f += s - n * x`. This accounts for products based on the rotated elements and their position in the rotated array. 
   - Update `max_f` to keep track of the maximum rotation product found so far: `max_f = max(max_f, f)`.  
4. **Return:** Return the maximum `max_f`.


## Complexity Analysis
* **Time Complexity:** $O(n)$ - We iterate through the array once in reverse order to calculate all rotations sums. 
    * The time complexity is linear as we perform a fixed number of operations (summation and comparisons) regardless of input size. 

* **Space Complexity:** $O(1)$ - The algorithm only uses constant space for variables like `s`, `f` and `max_f`.  We do not use any additional data structures, thus the space complexity is dominated by the variable sizes.