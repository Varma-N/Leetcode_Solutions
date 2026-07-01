# Problem 3660: Jump Game IX

## Intuition
The core idea is to use a stack data structure to keep track of the maximum value reachable from each index i after performing a valid jump. We iterate through the array, updating the `min_val` and `max_val` for each index `i`, taking into account the rules for jumps. This allows us to efficiently calculate the maximum values reachable at each point in the array.


## Approach
1. **Initialization:** 
   - Create an empty stack called `stack`.

2. **Iteration through the Array:** 
   - For each element `num` in the input array `nums`:
      - Initialize `min_val`, `max_val`, and `count` to `num`.

3. **Stack Pop and Comparison:**
   - While the stack is not empty and the top element of the stack has a value greater than `min_val`:
      - Pop the last element from the stack: 
         * `prev_min`, `prev_max`, and `prev_count` are extracted. 
         * Update `min_val` to be the minimum between `min_val` and `prev_min`. 
         * Update `max_val` to be the maximum between `max_val` and `prev_max`.
         * Increment `count` by `prev_count` (from the previous jump).
   - Append the new values `[min_val, max_val, count]` onto the stack.

4. **Result Calculation:**
   - Create an empty array `ans`. 
   - Iterate through the stack from top to bottom:
      * For each element in the stack (`[min_val, max_val, count]`) append `max_val` `count` times to `ans`.

5. **Return Result:**
   - Return the array `ans`.


## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The loop iterates through each element in the input array once.
* **Space Complexity:**  $O(N)$ 
    * We use a stack to store the maximum values reachable from each index, which can be at most `N` elements.