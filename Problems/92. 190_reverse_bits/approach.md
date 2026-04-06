# 190. Reverse Bits

## Problem Description
Reverse the bits of a given 32-bit unsigned integer.

---

## Step-by-Step Approach

To reverse the bits of a 32-bit integer, we process the input bit-by-bit from right to left and build the result from left to right.

1.  **Initialize Result:** Start with a variable `result` set to `0`. This will store the reversed bit sequence as it is built.
2.  **Constant Iteration:** Loop exactly **32 times**. This is necessary because even if the input number is small, we must account for all 32 positions (including leading zeros) to ensure they become trailing zeros in the reversed version.
3.  **Prepare the Result:** In each iteration, shift the current `result` to the left by 1 position. This creates an empty slot at the rightmost bit (least significant bit) for the next incoming bit.
4.  **Extract the Input Bit:** Isolate the rightmost bit of the input number `n` using a bitwise AND operation (`n & 1`).
5.  **Append to Result:** Use a bitwise OR operation to place the extracted bit into the empty slot created in the `result`.
6.  **Update the Input:** Shift the input number `n` to the right by 1 position. This discards the bit just processed and brings the next bit into the rightmost position for the next iteration.
7.  **Final Value:** After 32 cycles, return the `result` which now contains the bits in the correct reversed order.

---

## Complexity Analysis

* **Time Complexity:** **$O(1)$**
    * The algorithm always performs exactly 32 iterations, regardless of the input value. Since the number of operations is constant and does not scale with the size of the input, the complexity is $O(1)$.
* **Space Complexity:** **$O(1)$**
    * The algorithm only uses a single integer variable to store the result and a loop counter. No additional data structures are required, resulting in constant space complexity.
