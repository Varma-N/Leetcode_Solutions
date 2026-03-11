# 3379. Transformed Array

## Step-by-Step Approach

1.  **Initialize Variables**: Determine the length of the input array `nums` (denoted as `n`) and create a `result` array of size `n` initialized with zeros.
2.  **Iterate Through Indices**: Loop through each index `i` from `0` to `n-1`.
3.  **Check for Zero**: If `nums[i]` is `0`, set `result[i]` to `0`.
4.  **Calculate Transformed Index**: If `nums[i]` is not `0`, calculate the target index using modulo arithmetic to handle circular wrapping: `landing_index = (i + nums[i]) % n`.
5.  **Assign Value**: Set `result[i]` to the value found at `nums[landing_index]`.
6.  **Return Result**: After processing all elements, return the `result` array.

## Complexity Analysis

-   **Time Complexity**: $O(n)$
    -   We iterate through the array exactly once, performing constant-time operations for each element.
-   **Space Complexity**: $O(n)$
    -   We require an additional array of size `n` to store the transformed results.
