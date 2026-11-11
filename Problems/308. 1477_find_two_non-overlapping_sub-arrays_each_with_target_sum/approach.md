```markdown
# Problem 1477: Find Two Non-overlapping Sub-arrays Each With Target Sum

## Intuition
The problem asks to find two non-overlapping sub-arrays in an array that sum up to a given target value. The key insight is to consider the "two-sum" problem for each sub-array. This involves maintaining running sums and identifying sub-arrays that add up to the target. The algorithm uses dynamic programming to store the minimum sub-array lengths and use them to efficiently find the minimum sum of lengths.


## Approach
1. **Initialization:** 
   - Initialize a `min_lengths` array of size `n` to store the minimum lengths of sub-arrays ending at index `i`. 
   - Set `min_lengths[i]` to infinity, for all `i`.
   
2. **Two-Sum Loop:**
   -  Iterate through the array using `right` as the right boundary of the sub-array.
   -  For each `right`, calculate the running sum of the sub-array `current_sum` by adding `arr[right]`.
   - **Inner Loop for Sub-array Updates:**
     - `while current_sum > target and left <= right` : 
        -  Subtract `arr[left]` from `current_sum` to shrink the sub-array. 
        -  Increment `left` to move the boundary of the sub-array.
     - If `current_sum` becomes equal to `target`, 
        - Calculate `curr_len` as the length of the sub-array.
        - If `left > 0` and `min_lengths[left - 1]` is not infinity, update the minimum sum of lengths by comparing `curr_len + min_lengths[left - 1]` to the current `min_result`. 
        - Update `best_so_far` by finding the minimum length sub-array.
   -  Update `min_lengths[right]` with `best_so_far`.

3. **Result:**
   - If `min_result` is not infinity, return it as the minimum sum of lengths. 
   - Otherwise, return -1, indicating no sub-arrays were found.
 
## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The algorithm iterates through the array `N` times, and the inner loop executes at most `N` times. 
* **Space Complexity:** $O(N)$
    *  The `min_lengths` array is used to store the lengths of the minimum sub-arrays ending at each index.