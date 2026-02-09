# 1458. Max Dot Product of Two Subsequences

## Approach

### Intuition
The key insight is that we need to select matching elements from both arrays to maximize their product sum. Since we can skip elements from either array (but must maintain order), this is a classic dynamic programming problem similar to the Longest Common Subsequence pattern.

### Step-by-Step Approach

1. **Dynamic Programming Setup**:
   - Create a 2D DP table `dp` where `dp[i][j]` represents the maximum dot product using the first `i` elements of `nums1` and first `j` elements of `nums2`.
   - Initialize all values to a very small number (`-10^9`) to handle negative products correctly.

2. **State Transitions**:
   For each position `(i, j)` (1-indexed in DP table, 0-indexed in arrays):
   
   - **Option 1**: Take only the current product `nums1[i-1] * nums2[j-1]` (start a new subsequence)
   - **Option 2**: Add current product to the best result from previous positions `dp[i-1][j-1] + product` (extend existing subsequence)
   - **Option 3**: Skip current element from `nums1` → `dp[i-1][j]`
   - **Option 4**: Skip current element from `nums2` → `dp[i][j-1]`
   
   Choose the maximum of these four options as `dp[i][j]`.

3. **Base Case Handling**:
   - The DP table is initialized with very small values to ensure we never return an invalid "empty subsequence" result.
   - The recurrence naturally handles negative values by allowing us to start fresh with a single positive product when beneficial.

4. **Result Extraction**:
   - The answer is stored in `dp[m][n]` where `m` and `n` are the lengths of the input arrays.

### Why This Works
- By considering all four possibilities at each step, we explore every valid way to form subsequences.
- The DP table efficiently caches intermediate results, avoiding recomputation.
- Starting a new subsequence (Option 1) is crucial when previous products were negative and would reduce the total.

## Complexity Analysis

- **Time Complexity**: O(m × n), where `m` is the length of `nums1` and `n` is the length of `nums2`. We fill an `m×n` DP table with constant-time operations per cell.
- **Space Complexity**: O(m × n) for the DP table. This can be optimized to O(min(m, n)) using space compression, but the standard solution uses the full table for clarity.
