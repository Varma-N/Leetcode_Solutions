# Problem: Total Waviness of Numbers in Range II

## Approach

**Overview** <br>
Given the large constraint of $10^{15}$, a linear scan is computationally infeasible. Instead, this solution employs Digit Dynamic Programming (Digit DP) to efficiently calculate the total waviness of all integers up to a given limit $N$. The total waviness for the inclusive range `[num1, num2]` is evaluated using the prefix difference: $f(num2) - f(num1 - 1)$.

**Step 1: Prefix Evaluation Formulation** <br>
Define a primary function `solve(n_str)` that calculates the total waviness for all numbers in the range `[0, int(n_str)]`. 

**Step 2: State Definition (Digit DP)** <br>
Establish a recursive Depth-First Search (DFS) function parameterized to uniquely identify the state of the constructed digit sequence:
*   `idx`: The current positional index being evaluated in the string.
*   `is_tight`: A boolean constraining the current digit. If true, the chosen digit cannot exceed the corresponding digit in the upper bound string.
*   `is_lz`: A boolean tracking leading zeros. True if no non-zero digits have been placed yet.
*   `prev1`: The immediately preceding digit (or `-1` if unassigned).
*   `prev2`: The digit placed two indices prior (or `-1` if unassigned).

**Step 3: Base Case Formulation** <br>
If `idx` equals the length of the string, the number construction is complete. Return a tuple `(1, 0)`, signifying $1$ valid number configuration has been successfully formed, yielding $0$ additional waviness at the boundary.

**Step 4: Transition and Iteration** <br>
Determine the maximum permissible digit (`limit`) for the current position based on the `is_tight` flag. Iterate over all possible digits from $0$ to `limit`. For each digit `curr`, determine the subsequent tightness state (`nxt_tight`).

**Step 5: Leading Zero Processing** <br>
If `is_lz` is active:
*   If `curr` is $0$, the leading zero state continues. Recursively call the DFS with `prev1` and `prev2` remaining as `-1`.
*   If `curr` is non-zero, the leading zero state terminates. Pass `curr` as the new `prev1`, leaving `prev2` as `-1`.

**Step 6: Extrema (Waviness) Evaluation** <br>
Once out of the leading zero state, continuously evaluate the structural relationship of the digits. If both `prev1` and `prev2` are valid (not `-1`), verify if `prev1` acts as a local extremum:
*   **Peak:** `prev2 < prev1` and `prev1 > curr`
*   **Valley:** `prev2 > prev1` and `prev1 < curr`
If either condition is met, set a local `contribution` flag to $1$.

**Step 7: Combinatorial Aggregation** <br>
For valid non-leading-zero transitions, recursively determine the `ways` (number of valid suffixes) and `wave` (waviness accumulated in those suffixes). Update the state's total combinatorial count. Crucially, the total waviness for the current branch is augmented by `wave + (ways * contribution)`, as the current local peak or valley will appear in every valid suffix generated from this point.

**Step 8: State Memoization** <br>
Cache the aggregated `(total_ways, total_wave)` tuple in a memoization dictionary keyed by the current state variables. This eliminates redundant computations for overlapping subproblems.

## Complexity

*   **Time Complexity:** $O(D \cdot 10) = O(\log_{10}(N))$  <br>
    Where $D$ is the number of digits in the maximum boundary (up to 16 for $10^{15}$). The state space is bounded by the parameters: $D \times 2 \times 2 \times 11 \times 11 \approx 484 \cdot D$ states. For each state, the algorithm iterates up to $10$ times. Therefore, the time complexity is strictly proportional to the number of digits, resulting in $O(1)$ constant time operations relative to the problem constraints (or logarithmic relative to the magnitude of `num2`).
*   **Space Complexity:** $O(D) = O(\log_{10}(N))$ <br>
    The space footprint is governed by the maximum depth of the recursion stack and the capacity of the memoization dictionary. Both scale linearly with the number of digits $D$, rendering a highly optimal $O(D)$ auxiliary space complexity.