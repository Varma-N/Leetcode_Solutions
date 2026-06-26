# Problem 788: Rotated Digits

## Approach

### Step-by-Step Breakdown

1.  **Iterate Through the Range:**
    * Loop through every integer `i` from 1 up to `n` (inclusive).
2.  **Check for Invalid Digits:**
    * Convert the integer `i` to a string. 
    * If the number contains any "invalid" digits that do not transform into valid digits after a 180-degree rotation (specifically **3, 4, or 7**), the number cannot be "good." Skip to the next iteration.
3.  **Check for "Good" Condition:**
    * For a number to be "good," it must be a valid number after rotation *and* be different from the original number.
    * A number is guaranteed to be different from its rotated version if it contains at least one digit that changes upon rotation (**2, 5, 6, or 9**), provided it doesn't contain any invalid digits.
    * If the string contains at least one of these digits, increment the `count`.
4.  **Return Result:**
    * After the loop finishes, return the final `count` of good numbers found.

## Complexity Analysis

* **Time Complexity:** $O(N \cdot \log N)$
    * $N$ is the input number. For each integer up to $N$, we convert it to a string, which takes $O(\log N)$ time, and perform checks based on the number of digits.
* **Space Complexity:** $O(\log N)$
    * This is the space required to store the string representation of the current number being evaluated.