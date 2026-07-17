# Problem 1752: Check if Array Is Sorted and Rotated

## Intuition
The core idea is to check the array for a "single drop" pattern. If we encounter a descending order element (nums[i-1] > nums[i]), it indicates that the array might have been rotated, as each descending element would move forward in the sorted structure, potentially resulting in a single drop pattern.

## Approach
1. **Initialization:** 
   *  `drops = 0`: Initialize a counter to track if we encounter a "drop" (descending order).

2. **Iteration:** 
   * `for i in range(len(nums))`: Iterate through the array.
3. **Comparison:** 
   * `if nums[i-1] > nums[i]`: If the element to the left is greater than the current element (indicating a descending order), increment the `drops` counter.

4. **Result:**
   *  `return drops <= 1`: After checking all elements, if the count of "drops" is less than or equal to 1, return True, otherwise, return False.


## Complexity Analysis
* **Time Complexity:** $O(N)$ - We iterate through the array once (outer loop). 
    * The `if` condition inside the loop takes constant time per comparison. 

* **Space Complexity:** $O(1)$  - We use a constant amount of extra space for storing the `drops` variable and don't rely on any additional data structures other than basic array access.