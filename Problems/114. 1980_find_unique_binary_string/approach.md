# 1980. Find Unique Binary String

## Problem Description
Given an array of strings `nums` containing `n` unique binary strings each of length `n`, return a binary string of length `n` that does not appear in `nums`. If there are multiple answers, you may return any of them.

## Step-by-Step Approach: Cantor's Diagonal Argument

To find a binary string that is guaranteed not to be in the input list, we can use a constructive approach inspired by Cantor's Diagonal Argument. The goal is to build a string that differs from every string in the input list by at least one character.

1.  **Initialize an empty result string**: Start with an empty string (or a character array) that will eventually hold our unique `n`-length binary string.
2.  **Iterate through the indices**: Loop through the input array `nums` from index `i = 0` to `n - 1`.
3.  **Identify the "Diagonal" Character**: At each index `i`, look at the `i`-th character of the `i`-th string in the list (`nums[i][i]`).
4.  **Flip the character**: 
    * If `nums[i][i]` is `'0'`, append `'1'` to your result string.
    * If `nums[i][i]` is `'1'`, append `'0'` to your result string.
5.  **Guarantee Uniqueness**: By specifically changing the `i`-th character for the `i`-th string, the resulting string is guaranteed to be different from `nums[0]` at the first position, different from `nums[1]` at the second position, and so on.
6.  **Return the result**: Once the loop completes, the constructed string will have length `n` and will not match any string in the input array.

## Complexity Analysis

* **Time Complexity**: $O(n)$
    * We iterate through the list of strings exactly once. Inside the loop, we perform a constant time lookup and character append operation.
* **Space Complexity**: $O(1)$ (or $O(n)$ to store the output)
    * If we ignore the space required to hold the resulting string, the algorithm uses constant extra space. If counting the output string, the complexity is $O(n)$.
