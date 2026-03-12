# 3634. Minimum Removals to Balance Array

## Problem Description
Given an array of integers `nums` and an integer `k`, you need to remove the minimum number of elements from the array such that the remaining elements satisfy the following balance condition:

$$ \text{max}(remaining) \le k \times \text{min}(remaining) $$

Return the minimum number of elements to remove.

## Intuition
To minimize the number of removals, we must maximize the number of elements we keep. The condition depends solely on the minimum and maximum values of the subset of elements we choose to keep. 

If we sort the array, any valid subset of elements that satisfies the condition can be represented as a contiguous subarray within the sorted array. This is because if we fix the minimum element (`nums[left]`) and the maximum element (`nums[right]`) of our kept subset, any element `x` between them in the sorted order satisfies `nums[left] <= x <= nums[right]`. Since the condition only checks the global min and max of the subset (`nums[right] <= k * nums[left]`), including intermediate elements does not violate the condition and helps maximize the count of kept elements.

Therefore, the problem reduces to finding the **longest contiguous subarray** in the sorted `nums` such that the condition holds.

## Step-by-Step Approach

1.  **Sort the Array**: 
    Sorting allows us to efficiently manage the minimum and maximum values of any subarray using two pointers. In a sorted array, for any subarray `nums[left...right]`, `nums[left]` is the minimum and `nums[right]` is the maximum.

2.  **Initialize Pointers**: 
    Use a sliding window approach with two pointers, `left` and `right`, both starting at index 0. `left` represents the index of the minimum element in the current window, and `right` represents the index of the maximum element.

3.  **Expand the Window**: 
    Iterate `right` from 0 to `n - 1`. This expands the window to include `nums[right]` as the new potential maximum.

4.  **Shrink the Window (Validate Condition)**: 
    Check if the current window satisfies the condition: `nums[right] <= k * nums[left]`.
    - If `nums[right] > k * nums[left]`, the condition is violated. To fix this, we must increase the minimum value of the window. We do this by incrementing `left` until the condition is satisfied or the window becomes empty.

5.  **Track Maximum Keep**: 
    At each step, the current valid window size is `right - left + 1`. Update a variable `max_keep` to store the maximum window size found so far.

6.  **Calculate Result**: 
    The minimum number of removals is the total number of elements minus the maximum number of elements we can keep: `n - max_keep`.

## Complexity Analysis

### Time Complexity
$$ O(N \log N) $$
- **Sorting**: The initial sorting of the array takes $O(N \log N)$ time.
- **Sliding Window**: The `right` pointer iterates from 0 to $N-1$. The `left` pointer also increments at most $N$ times throughout the entire execution (it never resets). Thus, the two-pointer pass takes $O(N)$ time.
- **Total**: The dominant factor is the sorting step, resulting in $O(N \log N)$.

### Space Complexity
$$ O(1) \text{ or } O(N) $$
- **Auxiliary Space**: The algorithm uses a constant amount of extra space for variables (`left`, `right`, `max_keep`, etc.), which is $O(1)$.
- **Sorting Space**: Depending on the sorting implementation used by the language (e.g., Timsort in Python), the sorting step may require $O(N)$ space.
- **Total**: Generally considered $O(N)$ due to sorting requirements, or $O(1)$ if ignoring sorting space overhead.
