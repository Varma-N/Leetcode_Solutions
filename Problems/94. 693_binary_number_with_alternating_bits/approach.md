# 693. Binary Number with Alternating Bits - Logic & Approach

## Objective
Determine if a positive integer `n` has alternating bits (e.g., `10101`).

---

## Step-by-Step Implementation Logic

### 1. Neighbor Alignment via Bit-Shifting
To check if adjacent bits are different, we first need to align every bit with its immediate neighbor. We do this by shifting the entire binary pattern of `n` one position to the right.
* **Operation:** `n >> 1`
* **Visual:** If `n` is `1010`, the shifted version becomes `0101`.

### 2. Identifying Differences via XOR
The XOR (`^`) operation is the perfect tool for detecting differences because it returns `1` only when two bits are different.
* **Operation:** `x = n ^ (n >> 1)`
* **The Logic:** If `n` is perfectly alternating, every bit in `n` will be compared against its opposite bit in the shifted version.
* **The Result:** If alternating, `x` will result in a solid block of ones (e.g., `1111`). If there are any consecutive identical bits in `n`, a `0` will appear in the resulting pattern of `x`.

### 3. The "All Ones" Verification Trick
Instead of looping through `x` to see if all bits are `1`, we use a mathematical property of binary numbers.
* **Property:** A number composed entirely of ones (like `7`, which is `111`) is always exactly one less than a power of two (like `8`, which is `1000`).
* **The Check:** `(x & (x + 1))`
* **The Mechanism:** * When you add `1` to a block of ones (`0111`), a carry-over chain occurs, turning the pattern into its exact opposite (`1000`).
    * Performing a bitwise `AND` on two exact opposites results in `0`.
    * If `(x & (x + 1))` equals `0`, it proves `x` was a solid block of ones.

---

## Complexity Analysis

### Time Complexity: $O(1)$
The solution performs a fixed number of bitwise operations (Shift, XOR, Addition, AND). These are executed in constant time by the CPU regardless of the magnitude of the input integer (up to the word size of the system, e.g., 32-bit or 64-bit).

### Space Complexity: $O(1)$
The approach does not require additional data structures, string conversions, or recursion. It only uses a single variable to store the intermediate XOR result, resulting in constant space usage.
