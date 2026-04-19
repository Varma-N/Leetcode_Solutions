# 1680. Concatenation of Consecutive Binary Numbers

## Problem Summary
The goal is to concatenate the binary representations of all integers from `1` to `n` in order and return the decimal value of the resulting string modulo $10^9 + 7$.

## Step-by-Step Approach

### 1. Identify the Pattern of Concatenation
When we concatenate a new number `i` to an existing binary result, we aren't just adding it. We are shifting the existing result to the left to make "room" for the binary digits of `i`, and then placing `i` in that newly created space.
* **Formula:** $result = (result \times 2^{\text{length of } i}) + i$
* In bitwise terms: `(result << length_of_i) | i`

### 2. Determine Bit Length Dynamically
The number of bits required to represent `i` changes as `i` grows. Instead of calculating the bit length using strings or logarithms in every iteration, we can observe when the length increases:
* The bit length increases by 1 every time `i` reaches a new **power of 2** (e.g., 1, 2, 4, 8, 16...).
* **Efficient Check:** Use the bitwise trick `(i & (i - 1)) == 0` to identify if `i` is a power of 2. When this is true, increment the current `length` variable.

### 3. Iterative Construction
* Start with a `result` of 0 and a `length` of 0.
* Loop from `1` to `n`.
* Check for the power of 2 to update the `length`.
* Shift the current `result` to the left by the current `length` and add the current number `i`.
* Apply the modulo $10^9 + 7$ at each step to prevent integer overflow and keep the number within the required limits.

### 4. Handling Modulo
Since the concatenated binary string grows extremely fast, the decimal value will exceed standard integer limits quickly. Applying `% MOD` at every addition ensures the calculation remains efficient and correct.

---

## Complexity Analysis

### Time Complexity: $O(n)$
We iterate through the numbers from $1$ to $n$ exactly once. Inside the loop, we perform constant-time bitwise operations and additions.

### Space Complexity: $O(1)$
We only use a few integer variables (`result`, `length`, `MOD`) to keep track of the calculation, regardless of the size of $n$.
