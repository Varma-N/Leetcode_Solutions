# Approach: Greedy Construction with Multi-Phase Verification

The problem asks us to reconstruct a string of length $n$ that satisfies a given $n \times n$ Longest Common Prefix (LCP) matrix, or return an empty string if no such string can exist. The strategy relies on a multi-phase validation and greedy assignment technique.

---

## Step-by-Step Breakdown

### 1. Pre-Verification (Matrix Consistency Check)
Before attempting to build the string, we validate basic structural and mathematical properties that any valid LCP matrix must satisfy. We iterate through every pair $(i, j)$ and check:
*   **Symmetry:** $lcp[i][j]$ must equal $lcp[j][i]$.
*   **Self-LCP Bounds:** The LCP of a suffix with itself, $lcp[i][i]$, must be exactly equal to the length of that suffix, which is $n - i$.
*   **Value Range:** The LCP of two suffixes starting at $i$ and $j$ cannot exceed the remaining length of the shorter suffix: $lcp[i][j] \le n - \max(i, j)$.
*   **DP Transition Consistency:** If $lcp[i][j] > 0$, the characters at $i$ and $j$ match. Therefore, the common prefix length must be exactly $1$ plus the LCP of the remaining suffixes: $lcp[i][j] = 1 + lcp[i+1][j+1]$ (handling boundary conditions cleanly).

If any of these conditions are violated, it is mathematically impossible to form a string, and we immediately return `""`.

### 2. Greedy String Construction
If the matrix passes basic checks, we construct the string by mapping indices to integer character codes ($0$ for 'a', $1$ for 'b', etc.).
*   Initialize an array `chars` of size $n$ filled with $-1$ to represent unassigned characters.
*   Iterate through each index $i$ from $0$ to $n-1$:
    *   If `chars[i]` is already assigned, skip it.
    *   If it is unassigned, we must introduce a new character. We assign the next available character code (`current_char_code`).
    *   **Alphabet Limit:** If `current_char_code` reaches or exceeds $26$, it means the matrix requires more than 26 unique lowercase English letters, which is impossible. Return `""`.
    *   **Propagation:** Look ahead at all indices $j > i$. If $lcp[i][j] > 0$, it implies that `word[i]` must equal `word[j]`. We force-assign `chars[j]` to match `current_char_code`. If $j$ was already assigned a *different* character previously, a contradiction has occurred, so we return `""`.
*   Convert the completed `chars` array of integer codes into its actual lowercase string representation (`word`).

### 3. Post-Verification (Full DP Validation)
The greedy propagation ensures that characters match wherever $lcp[i][j] > 0$, but it does *not* guarantee that characters mismatch where $lcp[i][j] = 0$. To ensure absolute correctness, we must verify that our constructed string actually generates the exact input LCP matrix.
*   Initialize a 2D array `computed_lcp` of size $n \times n$ with zeros.
*   Compute the true LCP matrix for `word` using bottom-up Dynamic Programming, traversing from the bottom-right $(n-1, n-1)$ to the top-left $(0, 0)$.
*   For each cell $(i, j)$:
    *   If `word[i] == word[j]`, then `computed_lcp[i][j] = 1 + computed_lcp[i+1][j+1]` (clamping out-of-bounds transitions to $0$).
    *   If `word[i] != word[j]`, then `computed_lcp[i][j] = 0`.
*   **Early Mismatch Exit:** Immediately compare `computed_lcp[i][j]` with the input `lcp[i][j]`. If they do not match at any point, the constructed string is invalid, and we return `""`.

If the string successfully passes the DP validation phase, it is guaranteed to be correct, and we return `word`.

---

## Complexity Analysis

### Time Complexity
*   **Pre-Verification:** $\mathcal{O}(n^2)$ because we loop through all pairs of the $n \times n$ matrix.
*   **Greedy Construction:** $\mathcal{O}(n^2)$ due to the nested loop where each unassigned index scans forward up to $n$ elements to propagate characters.
*   **Post-Verification:** $\mathcal{O}(n^2)$ to fill out the dynamic programming state table for the generated string.
*   **Total Time Complexity:** $\mathcal{O}(n^2)$, which is optimal since we must read the input matrix of size $n \times n$.

### Space Complexity
*   **Character Mapping:** $\mathcal{O}(n)$ to store the temporary integer character array of size $n$ and the final string.
*   **DP Verification Table:** $\mathcal{O}(n^2)$ to store the `computed_lcp` state table used during the final verification phase.
*   **Total Space Complexity:** $\mathcal{O}(n^2)$ auxiliary space.
