# 1404. Number of Steps to Reduce a Number in Binary Representation to One

## Problem Description
Given the binary representation of an integer as a string `s`, return the number of steps to reduce it to `1` under these rules:
- If the current number is **even**, divide it by 2.
- If the current number is **odd**, add 1 to it.

The input string `s` is guaranteed to represent a positive integer and will not contain leading zeros.

---

## Step-by-Step Logic Analysis

Instead of converting the binary string into a large integer (which can lead to overflow in many languages) or repeatedly modifying the string (which is computationally expensive), we use a single-pass simulation from right to left.

### 1. Handling the Least Significant Bit (LSB)
We start from the end of the string (`n-1`) and move toward the beginning. This mimics how manual binary addition and bit-shifting work.

### 2. The Role of the "Carry"
When we encounter an odd number (LSB is `1`), the rules say we must add `1`. In binary, `1 + 1 = 10`. This creates a **carry** that ripples to the next bit. Once a carry is generated, it stays active until it is "absorbed" by a bit that was originally `0`.

### 3. Case-by-Case Breakdown (per bit)
For each bit at index `i` (from `n-1` down to `1`):
- **If (Bit + Carry) == 1**: 
    - This represents an **odd** state. 
    - We need two operations: Add 1 (to make it even) and Divide by 2 (the bit shift).
    - **Total Steps**: +2
    - **New Carry**: 1
- **If (Bit + Carry) == 0**:
    - This represents an **even** state.
    - We only need one operation: Divide by 2.
    - **Total Steps**: +1
    - **New Carry**: 0
- **If (Bit + Carry) == 2**:
    - This happens if a bit was `1` and we already had a `carry`.
    - It is effectively **even** because `1 + 1 = 10` (the `0` stays at the current position).
    - We only need one operation: Divide by 2.
    - **Total Steps**: +1
    - **New Carry**: 1 (the carry persists)

### 4. The Final Step
The loop stops before index `0`. At the end of the loop, if `carry` is `1`, it means the most significant bit (originally `1`) has become `2` (binary `10`). To reduce `10` to `1`, one final division step is required.

---

## Complexity Analysis

| Type | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | **O(N)** | We iterate through the string of length $N$ exactly once. Each operation inside the loop is $O(1)$. |
| **Space Complexity** | **O(1)** | We only maintain two integer variables (`steps` and `carry`) regardless of how large the input string is. |

---

## Edge Cases Considered
- **Input is "1"**: The loop does not run, and steps remain 0 (Correct, as it is already 1).
- **All ones ("111")**: The first bit creates a carry that ripples all the way through, testing the carry logic effectively.
- **Large Strings**: Since we avoid integer conversion, strings with lengths up to $10^5$ are handled without overflow.
