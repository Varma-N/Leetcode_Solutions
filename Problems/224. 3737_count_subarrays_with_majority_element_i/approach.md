# Problem 3737: Count Subarrays With Majority Element I

## Intuition
The core idea is to use a bit-array technique to efficiently count the number of subarrays where the target element appears more than half the time. This can be achieved by keeping track of the cumulative sum of elements in the array and then using this information to count subarrays that meet the majority element criteria.

## Approach
1. **Bit-Array for Cumulative Sum:** We initialize a bit-array `bit` with size `2*n+2`. This array serves as a cumulative sum tracker. 

    *  **`add(idx, val)`:** This function updates the bit-array at index `idx` by adding `val`. 
    *  **`query(idx)`:** This function returns the cumulative sum of elements up to index `idx`. 

2. **Dynamically Updating Subarray Counts:**
    *   **`ans`:** Initialize `ans` to store the total count of majority subarrays.
    *   **`curr_sum`:** Initialize a variable to track the cumulative sum of elements encountered in the array. 
    *   **`offset`:** Set `offset` to `n + 1` to represent the starting index for bit-array updates.
    *   **`add(curr_sum + offset, 1)`:** Initialize the bit-array `bit` with the starting value of `curr_sum + offset`, marking the initial point where the element is encountered.
    
3. **Iterating and Updating Counts:** 
    *   **`for num in nums`:**  We iterate through each element `num` in the `nums` array. 
        *   **`if num == target`:** If the current element is the target: Increment `curr_sum` by 1. 
        *   **`else`:** If the current element is not the target: Decrement `curr_sum` by 1. 
        *   **`ans += query(curr_sum + offset - 1)`:** Calculate the number of subarrays where the target element appears more than half the time using the `query` function.

 

## Complexity Analysis
* **Time Complexity:** $O(n)$ 
    *  The algorithm iterates through the input array once, performing a constant-time operation for each element. 
* **Space Complexity:** $O(n)$
    *  The bit-array used to maintain the cumulative sum has a size of `2n+2`, which is proportional to the input array size.