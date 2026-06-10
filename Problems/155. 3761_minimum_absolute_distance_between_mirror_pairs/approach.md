# Problem 3761: Minimum Absolute Distance Between Mirror Pairs

## Approach

### Step-by-Step Breakdown

1. **Reverse Numbers Efficiently**
   * Define a helper function `reverse_num` that reverses the digits of a number mathematically.
   * Leading zeros are automatically removed during reversal (e.g., `120 → 21`).

2. **Track Potential Mirror Matches**
   * Use a dictionary (`target_map`) where:
     * **Key:** A value that may appear in the future.
     * **Value:** The most recent index whose reversed value equals that key.
   * This allows constant-time lookup for mirror pair candidates.

3. **Process the Array from Left to Right**
   * For each index `j` and value `nums[j]`:
     * Check whether `nums[j]` already exists in `target_map`.
     * If it does, a previous index `i` satisfies `reverse(nums[i]) = nums[j]`.
     * Compute the distance `j - i` and update the minimum distance found so far.

4. **Prepare for Future Matches**
   * Compute `reverse(nums[j])`.
   * Store this reversed value as a future target in `target_map` with the current index.
   * This ensures later elements can quickly determine whether they form a mirror pair with the current number.

5. **Return the Result**
   * If at least one mirror pair was found, return the minimum distance.
   * Otherwise, return `-1`.

## Complexity Analysis

* **Time Complexity:** $O(N \cdot D)$
   * $N$ is the length of `nums`, and $D$ is the maximum number of digits in any number.
   * Each element is processed once, and reversing a number takes $O(D)$ time.

* **Space Complexity:** $O(N)$
   * The `target_map` dictionary may store up to one entry per processed element.
