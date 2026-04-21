# 1680. Concatenation of Consecutive Binary Numbers - Approach

## Problem Overview
The goal is to concatenate the binary representations of all integers from `1` to `n` in order and return the decimal value of the resulting binary string modulo $10^9 + 7$.

## Step-by-Step Approach

### 1. Identify the Pattern of Concatenation
When we concatenate a new number `i` to an existing binary result, we are effectively shifting the existing result to the left by the number of bits in `i`, and then adding the value of `i`.
- Mathematical representation: `result = (result << bit_length(i)) + i`

### 2. Efficiently Track Bit Length
Instead of calculating the bit length of every integer `i` using a function like `bin(i).length()`, we can observe that the bit length only increases by 1 when `i` is a power of 2 (e.g., 2, 4, 8, 16...).
- We can check if a number is a power of 2 using the bitwise check: `(i & (i - 1)) == 0`.

### 3. Iterative Construction
- Initialize `result = 0` and `length = 0`.
- Iterate through every integer from `1` up to `n`.
- For each integer `i`:
    - If `i` is a power of 2, increment the `length` tracker.
    - Shift the current `result` to the left by `length` bits.
    - Add the value of `i` to the `result`.
    - Apply the modulo $10^9 + 7$ at each step to prevent integer overflow.

### 4. Returning the Result
After the loop finishes, the `result` variable holds the decimal value of the concatenated binary string.

---

## Complexity Analysis

### Time Complexity: $O(n)$
The algorithm uses a single loop that iterates from $1$ to $n$. Inside the loop, all bitwise operations (shifting, bitwise AND) and additions are $O(1)$ operations. Therefore, the total time complexity is linear relative to $n$.

### Space Complexity: $O(1)$
The algorithm only uses a fixed number of integer variables (`result`, `length`, `MOD`) to store the state. No additional data structures or recursion are used, leading to constant space complexity.
