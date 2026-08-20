# Intuition

The problem asks us to find the number of subarrays where a specific `target` element appears strictly more than half the time. 

We can transform this into a prefix sum problem:
1. Treat every occurrence of the `target` as $+1$.
2. Treat every other element as $-1$.

A subarray has the `target` as the majority element if and only if the sum of its elements (after this transformation) is strictly greater than $0$. 
If we maintain a running prefix sum of these transformed values, a valid subarray from index $j+1$ to $i$ exists if `prefix_sum[i] - prefix_sum[j] > 0`, which simplifies to `prefix_sum[i] > prefix_sum[j]`. 

Instead of re-calculating or iterating through all past prefix sums for every new element (which would take $O(N^2)$ time), we can maintain a running count of how many past prefix sums are strictly smaller than our current prefix sum. Since the prefix sum only ever changes by $+1$ or $-1$ at each step, we can update this count dynamically in $O(1)$ time.

# Step-by-Step Approach

1. **Initialization:**
   * Create a `count` array of size $2N + 2$ to store the frequencies of each prefix sum we encounter. The prefix sum can range from $-N$ to $N$.
   * Use an `offset = N` to ensure all indices accessed in the `count` array are non-negative.
   * Initialize `count[offset] = 1` because we conceptually start with a prefix sum of $0$ before processing any elements.
   * Initialize `curr_sum = 0` (the running prefix sum).
   * Initialize `smaller_count = 0`, which will track how many previously seen prefix sums are strictly less than `curr_sum`.
   * Initialize `ans = 0` to store the total valid subarrays.

2. **Iterate Through the Array:**
   For each `num` in `nums`, we update our state based on whether `num` is the target or not:
   
   * **Case A: `num == target`**
     * The `curr_sum` will increase by $1$.
     * Because the sum increases, the old `curr_sum` is now strictly smaller than the new sum. 
     * We add the number of times we've previously seen the old `curr_sum` to `smaller_count`.
     * Finally, increment `curr_sum` by $1$.
     
   * **Case B: `num != target`**
     * The `curr_sum` will decrease by $1$.
     * Because the sum decreases, the new `curr_sum` is no longer strictly smaller than itself.
     * We must subtract the number of times we've previously seen the new `curr_sum` (which is `curr_sum - 1`) from `smaller_count`.
     * Finally, decrement `curr_sum` by $1$.

3. **Accumulate the Answer:**
   * At each step, `smaller_count` accurately reflects the number of valid starting indices for the current ending index. Add `smaller_count` to `ans`.
   * Record the new `curr_sum` in the `count` array by incrementing `count[curr_sum + offset]`.

4. **Return Result:**
   * After the loop finishes, `ans` holds the total number of valid subarrays.

# Complexity

* **Time Complexity:** $O(N)$
  We iterate through the `nums` array exactly once. In each iteration, updating the running sum, modifying the `smaller_count`, and updating the `count` array all take $O(1)$ time. Thus, the overall time complexity is linear.
  
* **Space Complexity:** $O(N)$
  We use a `count` array of size $2N + 2$ to keep track of the frequencies of the prefix sums, which requires linear extra space.