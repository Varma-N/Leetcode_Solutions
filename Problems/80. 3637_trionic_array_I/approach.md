# 3637. Trionic Array I

## Step-by-Step Approach

1.  **Base Case Check**
    *   If the array length `n` is less than 4, return `False`. A valid Trionic array requires at least 4 elements to form the pattern (Increasing → Decreasing → Increasing).

2.  **Compute Increasing Prefix (`inc_prefix`)**
    *   Create a boolean array where `inc_prefix[i]` is `True` if the subarray `nums[0...i]` is strictly increasing.
    *   Iterate from left to right: `inc_prefix[i] = inc_prefix[i-1] and (nums[i-1] < nums[i])`.

3.  **Compute Increasing Suffix (`inc_suffix`)**
    *   Create a boolean array where `inc_suffix[i]` is `True` if the subarray `nums[i...n-1]` is strictly increasing.
    *   Iterate from right to left: `inc_suffix[i] = (nums[i] < nums[i+1]) and inc_suffix[i+1]`.

4.  **Compute Decreasing Run Lengths (`dec_len`)**
    *   Create an integer array where `dec_len[i]` stores the length of the maximal strictly decreasing sequence starting at index `i`.
    *   Iterate from right to left: If `nums[i] > nums[i+1]`, then `dec_len[i] = dec_len[i+1] + 1`, otherwise `1`.

5.  **Optimize Suffix Lookup (`next_true`)**
    *   Precompute `next_true[i]`, which stores the smallest index `j >= i` such that `inc_suffix[j]` is `True`.
    *   This allows O(1) verification if a valid increasing suffix exists within a specific range during the final check.

6.  **Validate Trionic Condition**
    *   Iterate through each possible peak index `p` (from `1` to `n-3`).
    *   **Check Prefix**: Ensure `inc_prefix[p]` is `True`.
    *   **Check Decrease**: Ensure `dec_len[p] >= 2` (there is a decrease after `p`).
    *   **Check Suffix**: Calculate the maximum possible valley index `max_q` within the decreasing run. Use `next_true` to check if there exists any index `q` in `[p+1, max_q]` where the suffix becomes strictly increasing.
    *   If all conditions are met, return `True`.

7.  **Return Result**
    *   If the loop completes without finding a valid configuration, return `False`.

## Complexity Analysis

### Time Complexity
*   **O(N)**
*   The solution involves five separate linear passes over the array of size `n`:
    1.  Computing `inc_prefix`.
    2.  Computing `inc_suffix`.
    3.  Computing `dec_len`.
    4.  Computing `next_true`.
    5.  The final validation loop.
*   Since each pass is O(N), the total time complexity is linear.

### Space Complexity
*   **O(N)**
*   Four auxiliary arrays (`inc_prefix`, `inc_suffix`, `dec_len`, `next_true`) are created, each of size `n`.
*   Therefore, the space complexity is linear with respect to the input size.
