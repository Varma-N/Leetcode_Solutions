# Problem 2574: Left and Right Sum Differences

## Intuition
The core idea is to leverage the properties of arrays to efficiently calculate the difference between left and right sum at each index. By iterating through the array, we keep track of the current cumulative sums of elements on both sides.  This allows us to directly access these sums from the previous iteration, minimizing the number of calculations required.

## Approach
1. **Initialization:** 
   - `n`: Store the length of the input array `nums`.
   - `res`: Create an empty list to store the resulting difference values.
   - `current_left_sum`: Initialize a variable to track the cumulative sum on the left side of the array, initially set to 0.
   - `current_right_sum`: Initialize a variable to track the cumulative sum on the right side of the array, initially set to the sum of all elements in the array (`sum(nums)`).

2. **Iteration:** Loop through each index `i` from 0 to `n-1` in the input array:
   -  **Update `current_right_sum`:** Subtract `nums[i]` from the current `current_right_sum`, effectively calculating the sum of elements to the right of index `i`. 
   - **Calculate `res` value:** Calculate the absolute difference between `current_left_sum` and `current_right_sum` (`abs(current_left_sum - current_right_sum)`), which gives us the desired difference at index `i`, and append it to `res`. 
   - **Update `current_left_sum`:** Add `nums[i]` to `current_left_sum`, effectively calculating the sum of elements on the left side of index `i`.

3. **Return Result:** After iterating through all indices, return the `res` list containing the differences. 


## Complexity Analysis
* **Time Complexity:** $O(N)$: The algorithm traverses the array `nums` only once with a loop and calculates sums within each iteration, hence linear time complexity. 
    *  Explanation: We iterate through the input array to calculate each sum at each index. Therefore the number of operations is directly proportional to the array's length 'N'. 

* **Space Complexity:** $O(1)$: The algorithm uses a constant amount of extra space independent of the input size, as it only utilizes `res`,  `current_left_sum` and `current_right_sum`.
    *  Explanation: It leverages variables to track intermediate sums, but these are not stored beyond the scope of their calculation.