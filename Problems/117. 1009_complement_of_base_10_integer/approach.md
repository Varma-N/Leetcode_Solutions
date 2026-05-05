# 1009. Complement of Base 10 Integer

## Step-by-Step Approach

1.  **Handle Edge Case**: Check if the input number `n` is 0. Since the binary of 0 is "0", its complement is "1".
2.  **Calculate Bit Length**: Determine the number of bits used to represent `n` in binary (excluding leading zeros).
3.  **Generate a Bitmask**: 
    * Create a sequence of 1s that is the same length as the binary representation of `n`.
    * This is typically done using the formula: `mask = (1 << number_of_bits) - 1`.
4.  **Perform XOR Operation**:
    * XOR the input number `n` with the bitmask.
    * Logic: `n ^ 11...1` results in flipping every bit of `n` (0 becomes 1, and 1 becomes 0).
5.  **Return the Result**: The result of the XOR operation is the decimal integer representation of the complement.

## Complexity Analysis

* **Time Complexity**: **O(log N)**, where N is the input integer. The number of bits in a number is proportional to `log2(N)`.
* **Space Complexity**: **O(1)**, as no additional data structures proportional to the input size are used.
