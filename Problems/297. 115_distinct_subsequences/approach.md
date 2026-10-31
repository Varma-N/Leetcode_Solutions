# Problem 115: Distinct Subsequences

## Intuition
Generating all distinct subsequences of a string `s` that equals another string `t`.  We can solve this problem using dynamic programming. We can use a matrix (dp) to store the number of distinct subsequences. 


## Approach
1. **Initialization:**  
   * Create a dynamic programming matrix `dp` of size `(n+1) x (m+1)`, where `n` and `m` are the lengths of `s` and `t` respectively. 
   * Initialize `dp[0]` with 1. This accounts for the empty subsequence, which is always valid. 
2. **Iterative Calculation:**
   * For each character in `s` (from index 1 to `m`), iterate through the characters in `t` (from index `n` to 1). 
   * If the characters `s[i-1]` and `t[j-1]` are equal: 
       * Increment the `dp[j]` entry. 
       *  This accounts for the valid subsequence. 
   * `dp[j]` will store the number of distinct subsequences of `s` ending at index `i` that match `t` up to index `j`.
3. **Result:**
   * After iterating through all characters, `dp[n]` represents the total number of distinct subsequences of `s` that equal `t`. 


## Complexity Analysis
* **Time Complexity:** $O(mn)$ 
    * We iterate through each character in `s` once and each character in `t` once.
* **Space Complexity:** $O(n)$
    * We need a `dp` matrix of size `(n+1) x (m+1)` to store the number of distinct subsequences.