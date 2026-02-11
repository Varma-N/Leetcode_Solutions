# Minimum ASCII Delete Sum for Two Strings (LeetCode 712)

## Intuition

We want to make two strings **equal** by deleting characters from either string, while minimizing the **total ASCII value** of the deleted characters.

Key observations:
- Deletions are allowed from **both strings**.
- If two characters are equal, we should **keep them** (no cost).
- If they are different, we must delete **one of them**, paying its ASCII value.
- The optimal choice at each position depends on optimal solutions of smaller suffixes → **dynamic programming**.

This problem can be viewed as a **cost-based variant of LCS**, where instead of maximizing the kept characters, we minimize the deletion cost.

---

## Step-by-Step Approach

1. Define `dp[i][j]` as the **minimum ASCII delete sum** needed to make  
   `s1[i:]` and `s2[j:]` equal.
2. Compute the solution **bottom-up**, starting from the ends of both strings.
3. Base cases:
   - If `s2` is exhausted (`j == n`), delete all remaining characters in `s1`.
   - If `s1` is exhausted (`i == m`), delete all remaining characters in `s2`.
4. Transition:
   - If `s1[i] == s2[j]`  
     → no deletion cost  
     → `dp[i][j] = dp[i + 1][j + 1]`
   - Otherwise:
     - Delete `s1[i]` → `ord(s1[i]) + dp[i + 1][j]`
     - Delete `s2[j]` → `ord(s2[j]) + dp[i][j + 1]`
     - Take the minimum of the two.
5. The final answer is `dp[0][0]`.

---

## Why This Works

- Each state `(i, j)` represents the optimal solution for suffixes starting at `i` and `j`.
- Overlapping subproblems are reused via the DP table.
- Bottom-up computation ensures all required sub-results are already known.
- Local optimal choices lead to a globally optimal solution.

---

## Time Complexity

- **Time:** `O(m × n)`  
  Each DP state is computed once.
- **Space:** `O(m × n)`  
  A 2D DP table is used to store results for all suffix combinations.

---

## Key Insight

Instead of focusing on **which characters to keep**, focus on **which characters to delete** and assign a cost to each deletion.  
This perspective simplifies the problem into a clean and efficient dynamic programming solution.
