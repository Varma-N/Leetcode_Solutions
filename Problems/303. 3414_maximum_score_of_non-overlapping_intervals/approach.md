# Problem 3414: Maximum Score of Non-overlapping Intervals

## Intuition
Given a set of intervals, the goal is to select the non-overlapping intervals with the highest total weight. This can be achieved by sorting intervals based on their starting points and dynamically building a score table to evaluate different options.


## Approach
1. **Sorting:**  Sort the intervals based on their starting points using `bisect_right` to create a sorted sequence.  
2. **Initialization:**  Initialize `prev_dp` (a list of tuples) to store the highest weight achievable for each index i.
3. **Dynamic Programming:**
   * **Iteration:**  Iterate over the sorted intervals using a loop.
   * **Next Index:**  Determine the next index in the `next_idx` list using `bisect_right` to check for overlapping intervals.
   * **Previous Values:**  Get the previous maximum weight and the corresponding list of indices from `prev_dp` using `prev_dp[next_idx[i]]`.
   * **Score Calculation:**  Calculate the score for the current interval by comparing the current weight with the maximum weight achievable for the next index.
4. **Return:**  Return the indices of the highest score intervals. 

### Complexity Analysis
* **Time Complexity:** $O(N log N)$
    * Sorting the intervals: $O(N log N)$
    * Dynamic programming: $O(N)$
* **Space Complexity:** $O(N)$
    * `prev_dp` list: $O(N)$