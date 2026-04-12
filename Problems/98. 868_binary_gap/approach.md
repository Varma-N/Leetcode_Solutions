# Binary Gap Approach

## Step-by-Step Approach

1.  **Initialize Tracking Variables**: 
    * Set a variable `last_index` to -1 to represent that no '1' bit has been encountered yet.
    * Set a `current_index` to 0 to track the current bit position being inspected.
    * Set `max_distance` to 0 to store the largest gap found between consecutive ones.

2.  **Bitwise Traversal**:
    * Enter a loop that continues as long as the integer `n` is greater than 0.
    * Isolate the rightmost bit (least significant bit) using the bitwise AND operator (`n & 1`).

3.  **Check for '1' Bits**:
    * If the current bit is `1`:
        * Check if `last_index` is no longer -1 (meaning this is at least the second '1' found).
        * If it is the second '1' or later, subtract `last_index` from `current_index` to find the gap length.
        * Update `max_distance` if this new gap is larger than the previous maximum.
        * Update `last_index` to the `current_index` to prepare for the next potential gap.

4.  **Bit Manipulation and Incrementation**:
    * Shift the bits of `n` to the right by one position (`n >>= 1`) to bring the next bit into the least significant position.
    * Increment the `current_index` by 1 to maintain the correct position count.

5.  **Final Output**:
    * Once the loop finishes (when `n` reaches 0), return the `max_distance`. If the number had one or zero '1's, the result will correctly be 0.

---

## Complexity

* **Time Complexity**: $O(\log n)$, because the number of iterations is equal to the number of bits in the binary representation of the integer $n$.
* **Space Complexity**: $O(1)$, as the algorithm uses a fixed amount of space for variables regardless of the size of the input.
