# 1758. Minimum Changes To Make Alternating Binary String

## Problem Description
Given a string `s` consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called **alternating** if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the **minimum** number of operations needed to make the string alternating.

---

## Step-by-Step Approach

### 1. Identify the Target Patterns
An alternating binary string of length `n` can only start in two ways:
* **Pattern A:** Starts with '0' (e.g., `010101...`)
* **Pattern B:** Starts with '1' (e.g., `101010...`)

### 2. Compare with Pattern A
We calculate how many changes are needed to transform the input string `s` into **Pattern A** (starting with '0').
* If the index `i` is even (`i % 2 == 0`), the character should be `'0'`.
* If the index `i` is odd (`i % 2 != 0`), the character should be `'1'`.
* Every time the character at `s[i]` does not match this rule, we increment a counter (let's call it `diff`).

### 3. Calculate for Pattern B (The Optimization)
A key observation is that **Pattern B** is simply the inverse of **Pattern A**. 
* If a character needs to be changed to fit Pattern A, it *already* fits Pattern B.
* If a character fits Pattern A, it *needs* to be changed to fit Pattern B.
* Therefore, the number of operations for Pattern B is simply: `Total Length - diff`.

### 4. Find the Minimum
The result is the smaller value between the operations needed for Pattern A and the operations needed for Pattern B.
`result = min(diff, length_of_s - diff)`

---

## Complexity Analysis

### Time Complexity
**O(n)**
We iterate through the string exactly once to compare each character with the expected alternating value. Here, `n` is the length of the string `s`.

### Space Complexity
**O(1)**
We only use a single integer variable (`diff`) to keep track of the mismatches. No additional data structures proportional to the input size are required.
