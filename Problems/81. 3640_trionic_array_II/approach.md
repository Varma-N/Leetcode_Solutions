# Approach: Trionic Array II

## Problem Understanding
The goal is to find the maximum sum of a subarray that follows a **Trionic** pattern: **Strictly Increasing → Strictly Decreasing → Strictly Increasing**. 

Mathematically, we need to select indices $i, j, k, l$ such that:
1.  $nums[i \dots j]$ is strictly increasing.
2.  $nums[j \dots k]$ is strictly decreasing.
3.  $nums[k \dots l]$ is strictly increasing.
4.  The sum $nums[i \dots l]$ is maximized.

This can be rewritten using Prefix Sums as maximizing $pref[l+1] - pref[i]$, subject to the structural constraints between $i, j, k, l$.

## Step-by-Step Algorithm

### 1. Prefix Sum Calculation
Compute a prefix sum array `pref` where `pref[x]` is the sum of `nums[0...x-1]`. This allows $O(1)$ calculation of any subarray sum.

### 2. Boundary Precomputation
To efficiently validate the increasing/decreasing segments, precompute three arrays in $O(N)$:
*   `left_inc[i]`: The starting index of the longest strictly increasing sequence ending at `i`.
*   `right_inc[i]`: The ending index of the longest strictly increasing sequence starting at `i`.
*   `left_dec[i]`: The starting index of the longest strictly decreasing sequence ending at `i`.

### 3. Optimize First Segment (Minimum Start)
For every possible **peak** index `i` (end of the first increasing segment), we want to find the minimum prefix sum `pref[start]` such that `start` is within the valid increasing range `[left_inc[i], i-1]`.
*   Use a **Monotonic Queue** to maintain indices with increasing prefix sums.
*   Store the result in `m_arr[i]`.
*   Time Complexity: $O(N)$.

### 4. Optimize Third Segment (Maximum End)
For every possible **valley** index `i` (end of the decreasing segment), we want to find the maximum prefix sum `pref[end]` such that `end` is within the valid increasing range `[i+2, right_inc[i]+1]`.
*   Use a **Sparse Table** to perform Range Maximum Queries (RMQ) on the `pref` array.
*   Store the result in `M_arr[i]`.
*   Time Complexity: $O(N \log N)$ for construction, $O(1)$ per query.

### 5. Combine Segments
Iterate through each index `q` considering it as the **valley** (end of the decreasing segment).
*   We need to pair `q` with a valid **peak** `p` such that the decreasing segment `nums[p...q]` is valid (i.e., `p >= left_dec[q]`).
*   Maintain a second **Monotonic Queue** (`dq_peaks`) that stores potential peaks `p`. This queue keeps `m_arr[p]` in increasing order.
*   For each `q`:
    1.  Remove invalid peaks from the front of `dq_peaks` (where `p < left_dec[q]`).
    2.  If valid peaks exist, calculate candidate sum: `M_arr[q] - m_arr[dq_peaks[0]]`.
    3.  Update the global maximum.
    4.  Add current `q` as a potential peak for future valleys (if `m_arr[q]` is valid).
*   Time Complexity: $O(N)$.

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time** | $O(N \log N)$ | Dominated by the Sparse Table construction. All other steps (prefix sums, boundary arrays, monotonic queues) are linear $O(N)$. |
| **Space** | $O(N \log N)$ | Required to store the Sparse Table. The auxiliary arrays and queues take $O(N)$. |
