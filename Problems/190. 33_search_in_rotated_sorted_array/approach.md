# Problem 33: Search in Rotated Sorted Array

## Intuition
The key insight is to utilize binary search, a highly efficient algorithm for searching within sorted data.  Since the array might be rotated, we strategically employ two pointers (`left` and `right`) to narrow down the search space based on the array's structure. By examining the array from the left and comparing it with the target value, we determine whether it lies in the left half or right half. This process helps us refine the search space until a match is found or the entire array has been traversed.


## Approach
1. **Initialization**: 
   - We initialize `left` pointer to 0 (the beginning of the array) and `right` pointer to `len(nums) - 1` (the end of the array). This sets our search boundaries for binary search.

2. **Binary Search Loop**:
   - We perform a binary search until we find the target or exhaust all possibilities (`left` > `right`).
      - Calculate the `mid` index: `mid = (left + right) // 2`.  This effectively splits the array in half at each step.
      - **Comparison:** We check if `target` is equal to `nums[mid]`. If yes, we've found the target! Return its index (`mid`).

   - **Determine Search Space**: Based on whether `target` is smaller than or greater than the current middle element,  we narrow down our search space:
      -  **Case 1:** if  `nums[left] <= nums[mid]` (meaning the target might be in the left half): 
         - We use a conditional statement to check if `target` lies within the range of `nums[left]` to `nums[mid]`. If it does, then we update `right` to  `mid - 1`, indicating that the search should focus on the left half. If not, we move `left` to `mid + 1` (shifting the target search area further).
      - **Case 2:** if `nums[left]` is greater than `nums[mid]` (meaning the target might be in the right half):
         - We use a conditional statement to check if `target` lies within the range of `nums[mid]` to `nums[right]`. If it does, then we update `left` to  `mid + 1`, indicating that the search should focus on the right half. If not, we move `right` to `mid - 1` (shifting the target search area further).

3. **Target Not Found**:
   - If the loop completes without finding a match (`left > right`), it means the target is not in the array.  We return -1.


## Complexity Analysis
* **Time Complexity:** $O(log n)$ 
    * Binary Search: Each iteration of the `while` loop reduces the search space by half, leading to logarithmic complexity.

* **Space Complexity:** $O(1)$ 
    * We use a fixed amount of memory (constant in terms of `nums` size) for our pointer variables and the result variable. This does not scale with the input array's size, thus it is constant space complexity.