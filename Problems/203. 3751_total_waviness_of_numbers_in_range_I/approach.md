# Problem: 3571. Total Waviness of Numbers in Range I

## Approach

**Step 1: State Initialization** <br>
Initialize an accumulator variable to track the total sum of peaks and valleys across all numbers in the specified domain.

**Step 2: Range Iteration** <br>
Iterate sequentially through the inclusive numerical range `[num1, num2]`. 

**Step 3: String Type Casting** <br>
Cast each integer to its string representation. This structural transformation facilitates $O(1)$ indexed access to individual digits, enabling efficient positional comparisons.

**Step 4: Interior Digit Traversal** <br>
For each string, iterate through its interior characters. By restricting the iteration bounds to the interval `[1, length - 2]`, the algorithm intrinsically bypasses the first and last digits, strictly adhering to the constraint that boundary digits cannot qualify as extrema.

**Step 5: Extrema Evaluation** <br>
Evaluate the local neighborhood of the current digit at index `i`:
*   **Peak Identification:** Determine if the current digit is strictly greater than both its predecessor (`i - 1`) and successor (`i + 1`).
*   **Valley Identification:** Determine if the current digit is strictly less than both its predecessor (`i - 1`) and successor (`i + 1`).

**Step 6: Accumulator Update** <br>
If the current digit satisfies either the peak or the valley condition, increment the total waviness accumulator by 1.

**Step 7: Final Yield** <br>
Upon exhaustion of the numerical range, return the final accumulated waviness count.

## Complexity

*   **Time Complexity:** $O(N \cdot D)$ <br>
    Where $N$ is the number of integers in the range (`num2 - num1 + 1`) and $D$ is the maximum number of digits in those integers. Because the constraints specify `num2 <= 10^5`, $D$ is at most 6. Thus, the time complexity scales linearly with the size of the range, simplifying to $O(N)$.
*   **Space Complexity:** $O(D)$ <br>
    This space is required to store the string representation of each number during the iteration. Since the maximum length of the string is 6 characters, this effectively resolves to $O(1)$ auxiliary space complexity.