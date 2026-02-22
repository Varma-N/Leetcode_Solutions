# LeetCode 3314: Construct the Minimum Bitwise Array I

## Problem Statement
Given an integer array `nums`, construct an array `ans` where `ans[i]` is the smallest non-negative integer `x` such that `x OR (x + 1) == nums[i]`. If no such integer exists, `ans[i]` should be `-1`.

## Approach

The solution relies on analyzing the binary properties of the operation `x | (x + 1)`.

### Key Insights
1.  **Parity Constraint**: The result of `x | (x + 1)` is always an **odd number**. This is because `x` and `x+1` differ only in the trailing bits; specifically, one ends in `0` and the other in `1`. The OR operation at the least significant bit will always yield `1`. Therefore, if `nums[i]` is even (specifically `2` in this problem's constraints), no solution exists.
2.  **Trailing Ones Pattern**: 
    - If `x` ends in `k` zeros (e.g., `...100...0`), then `x+1` ends in `k` ones (e.g., `...100...1` -> `...101...1`? No, carry propagates).
    - Actually, consider the reverse: If `p = x | (x+1)`, `p` must end with a sequence of `1`s.
    - Let `t` be the count of consecutive `1`s at the end of `p` (trailing ones).
    - To get the **smallest** `x`, we want to change the lowest possible bit of `p` from `1` to `0` such that adding `1` to `x` restores that bit via carry propagation without affecting higher bits unnecessarily.
3.  **Formula Derivation**:
    - If `p` has `t` trailing ones, the smallest `x` is obtained by subtracting $2^{t-1}$ from `p`.
    - Mathematically: `x = p - (1 << (t - 1))`.
    - This effectively turns the least significant `1` of the trailing block into a `0`.

### Step-by-Step Algorithm
1.  Initialize an empty list `ans`.
2.  Iterate through each number `p` in `nums`:
    - **Check Validity**: If `p == 2` (or generally any even number where logic fails), append `-1`.
    - **Count Trailing Ones**: Initialize `t = 0`. While the least significant bit of `p` is `1`, increment `t` and right-shift `p` (using a temporary variable).
    - **Calculate Minimum x**: Apply the formula `x = p - (1 << (t - 1))`.
    - Append `x` to `ans`.
3.  Return `ans`.

## Complexity Analysis

- **Time Complexity**: $O(N \cdot B)$
  - $N$ is the number of elements in `nums`.
  - $B$ is the number of bits in the integer (max ~30 for $10^9$).
  - Since $B$ is constant, the effective time complexity is **$O(N)$**.
  
- **Space Complexity**: $O(1)$
  - Excluding the output array, we only use a few integer variables for storage. No additional data structures are proportional to input size.

## Example Walkthrough

**Input**: `nums = [7, 10, 15]`

1.  **For `p = 7`** (`111` in binary):
    - Trailing ones `t = 3`.
    - Calculation: $x = 7 - 2^{3-1} = 7 - 4 = 3$.
    - Verification: $3 | 4 \rightarrow 011 | 100 = 111 (7)$. ✅
    
2.  **For `p = 10`** (`1010` in binary):
    - Even number (and specifically handled as impossible case `2` or derived logic).
    - Result: `-1`.

3.  **For `p = 15`** (`1111` in binary):
    - Trailing ones `t = 4`.
    - Calculation: $x = 15 - 2^{4-1} = 15 - 8 = 7$.
    - Verification: $7 | 8 \rightarrow 0111 | 1000 = 1111 (15)$. ✅

**Output**: `[3, -1, 7]`
