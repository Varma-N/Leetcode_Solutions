# Minimum Number of Flips to Make the Binary String Alternating

## Step-by-Step Approach

1. **Simulate Rotations via String Concatenation**  
   Instead of physically rotating the string, concatenate it with itself (`s + s`). Every contiguous substring of length `n` in this doubled string represents a unique cyclic shift of the original string, allowing us to evaluate all possible Type 1 operations in a single pass.

2. **Precompute Mismatch Indicators**  
   Iterate through the doubled string and compare each character against a single base alternating pattern that starts with `'0'` (`010101...`). Store `1` at indices where a mismatch occurs and `0` otherwise. This array acts as a quick lookup for flip costs.

3. **Initialize the First Window**  
   Sum the mismatch values for the first substring (indices `0` to `n-1`). This sum equals the flips required to match the base `'0'`-starting pattern. Because the `'1'`-starting pattern is its exact bitwise complement, its cost is simply `n - current_diff`. Initialize the global minimum with `min(current_diff, n - current_diff)`.

4. **Slide the Window Across All Rotations**  
   Move the window one character at a time from index `1` to `n-1`. At each step:
   - Subtract the mismatch value leaving the window (`mismatches[i - 1]`).
   - Add the mismatch value entering the window (`mismatches[i + n - 1]`).
   This maintains an up-to-date flip count for the current rotation in $O(1)$ time.

5. **Track the Minimum Across Both Patterns**  
   After each slide, recalculate `min(current_diff, n - current_diff)` and update the global minimum if a smaller value is found. This ensures we capture the optimal flip count for both possible alternating targets at every rotation.

6. **Return the Final Result**  
   After evaluating all `n` valid cyclic shifts, the tracked minimum value represents the least number of Type 2 operations needed to make the string strictly alternating under optimal rotation.

## Time and Space Complexity

- **Time Complexity:** $\mathcal{O}(n)$  
  The algorithm performs two linear passes over a string of length $2n$: one to precompute mismatches and another to slide the window across all $n$ rotations. Each step involves only constant-time arithmetic and comparisons, resulting in overall linear time.

- **Space Complexity:** $\mathcal{O}(n)$  
  An auxiliary array of size $2n$ is used to store mismatch indicators. All other variables use constant extra space, yielding a linear space footprint relative to the input size.
