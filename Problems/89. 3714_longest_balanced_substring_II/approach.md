# 3714. Longest Balanced Substring II - Approach

## Step-by-Step Approach

### Step 1: Handle Single Character Substrings
The simplest form of a balanced substring is one that contains only a single type of character.
- Iterate through the string to find the longest contiguous run of identical characters.
- Maintain a counter for the current run length and update a global maximum whenever the current run exceeds it.
- Reset the counter whenever the character changes.

### Step 2: Handle Three Character Balance (a = b = c)
To find the longest substring where the counts of 'a', 'b', and 'c' are all equal, use the **Prefix Sum Difference** technique.
- Maintain running counts for 'a', 'b', and 'c' as we iterate through the string.
- Instead of storing the absolute counts, store the **differences** between them relative to 'a'. Specifically, track `(count_a - count_b)` and `(count_a - count_c)`.
- Use a hash map to store the first index where a specific pair of differences `(diff1, diff2)` occurs.
- If the same pair of differences appears again at a later index, it means the net change in counts between the two indices is zero for all three characters.
- Calculate the length of this substring and update the maximum length found so far.

### Step 3: Handle Two Character Balance (x = y, z = 0)
Check pairs of characters ('a' & 'b', 'a' & 'c', 'b' & 'c') where the third character is absent.
- Iterate through all three possible permutations of character pairs. For each permutation, treat two characters as the target pair (X, Y) and the third as a delimiter (Z).
- Perform a linear scan similar to the "Contiguous Array" problem:
  - Treat character X as `+1` and character Y as `-1`.
  - If character Z is encountered, it breaks the continuity. Reset the current sum and clear the history map because the substring cannot contain Z.
  - Use a hash map to store the first index where a specific cumulative sum occurs.
  - If the same sum is encountered again, it indicates a balanced substring between the two indices (equal number of X and Y).
- Track the maximum length found across all three permutations.

### Step 4: Combine Results
- The final answer is the maximum value obtained from the three steps above.
- Return this maximum value as the result.

## Complexity Analysis

### Time Complexity
- **Single Character Scan:** $O(N)$, where $N$ is the length of the string.
- **Three Character Balance:** $O(N)$, as we iterate through the string once and perform constant-time hash map operations.
- **Two Character Balance:** $O(3 \times N) \approx O(N)$, as we iterate through the string three times (once for each pair permutation).
- **Total Time Complexity:** $O(N)$

### Space Complexity
- **Hash Maps:** In the worst case, the hash maps used for storing prefix differences or sums can store up to $O(N)$ entries.
- **Total Space Complexity:** $O(N)$
