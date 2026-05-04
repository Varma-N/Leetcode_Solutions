# Approach: Find All Possible Stable Binary Arrays II

## Problem Understanding
The goal is to find the number of binary arrays containing exactly `zero` 0s and `one` 1s such that no more than `limit` consecutive elements are the same. We use Dynamic Programming to count these valid permutations.

## Approach: 3D Dynamic Programming with Sliding Window Sum

### 1. State Definition
We define `dp[i][j][k]` as the number of stable binary arrays with:
- `i` zeros used.
- `j` ones used.
- `k` representing the last element added (0 or 1).

### 2. Base Case Initialization
- At the start (`i=0, j=0`), there is effectively 1 way to have an empty array.
- We set `dp[0][0][0] = 1` and `dp[0][0][1] = 1` as foundations for the transitions.

### 3. Transition Logic (Iterative Filling)
We iterate through all possible counts of zeros ($0$ to `zero`) and ones ($0$ to `one`).

#### Case A: Ending with 0 (`dp[i][j][0]`)
To form an array of length $(i+j)$ ending in 0:
- **Base Transition:** We can append a 0 to any stable array of length $(i-1+j)$ that ended in either 0 or 1.
- **Constraint Handling (The Limit):** We must subtract arrays that would violate the limit. If we add a 0 and it results in `limit + 1` consecutive zeros, that sequence is invalid.
- **Subtraction Logic:** If $i > limit$, we subtract the cases where the sequence *must* have just completed a streak of `limit` zeros. This specifically happens if we had a 1 followed by exactly `limit` zeros.

#### Case B: Ending with 1 (`dp[i][j][1]`)
To form an array of length $(i+j)$ ending in 1:
- **Base Transition:** Append a 1 to any stable array of length $(i+j-1)$ that ended in either 0 or 1.
- **Constraint Handling:** Similar to the zero case, if $j > limit$, we subtract the configurations where adding this 1 creates a streak of `limit + 1` ones.

### 4. Edge Case Handling
- If $i=0$ (no zeros available), `dp[i][j][0]` is naturally 0.
- If $j=0$ (no ones available), `dp[i][j][1]` is naturally 0.
- Special subtractions are made when $i=1$ or $j=1$ to account for the initial base case setup and avoid overcounting.

### 5. Final Result
The final answer is the sum of stable arrays ending in 0 and those ending in 1 with the total counts:
`Result = (dp[zero][one][0] + dp[zero][one][1]) % MOD`

---

## Complexity Analysis

### Time Complexity: $O(\text{zero} \times \text{one})$
We use a nested loop that iterates through the total number of zeros and ones once. The transitions inside the loop (including the limit check) are $O(1)$ due to the mathematical subtraction logic.

### Space Complexity: $O(\text{zero} \times \text{one})$
We maintain a 3D DP table of size `(zero + 1) * (one + 1) * 2`. In optimized versions, this can sometimes be reduced to 2D using space-optimization techniques, but the standard approach uses $O(N \times M)$ space.
