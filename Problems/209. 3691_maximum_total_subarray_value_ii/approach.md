# Problem 3691: Maximum Total Subarray Value II

## Intuition
The core idea is to use a dynamic programming approach to build up the maximum sum of subarrays. By using a two-dimensional table `mx` and `mn`, we can calculate the maximum and minimum values for each subarray in a sliding window manner, then calculate the total value by summing the differences between those ranges.  The algorithm leverages the fact that the subarray's range will be limited to the largest possible range based on the input array. This allows us to effectively explore all subarrays within this bound.


## Approach
1. **Logarithmic Complexity:**
   - We use a precalculated logarithmic value `lg` for each length to determine optimal subarray ranges. 
2. **Initialization:**
   - Initialize the table `mx`, `mn` and calculate the maximum and minimum values for each starting index `i` in the input array.
3. **Dynamic Programming (Sliding Window):**
   - For each step of our sliding window, we update the maximum and minimum values at each start index by comparing the previous results with the current range's maximum and minimum values. 
4. **Heap Processing:**
   - A min-heap is used to store subarrays and their corresponding total values, prioritizing those with smaller differences (i.e., higher negative value) for quicker retrieval.

## Complexity Analysis
* **Time Complexity:** $O(n * log(n))$
    * The precalculating logarithmic complexity `lg` takes O(n) time
* **Space Complexity:** $O(n)$ 
    * We store two arrays of size n to hold the maximum and minimum values for each subarray, along with a heap of size k.