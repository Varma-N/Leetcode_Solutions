# Four Divisors - Approach

## Step-by-Step Logic

1. **Process each number independently**: Iterate through every integer `n` in the input array.

2. **Efficient divisor enumeration**: 
   - Scan potential divisors from `1` to `√n` (inclusive)
   - For each divisor `i` found (`n % i == 0`), capture both the divisor `i` and its complementary pair `n/i`
   - Store divisors in a set to automatically handle duplicates (critical for perfect squares)

3. **Early termination optimization**: 
   - Immediately abort the divisor scan if the set size exceeds 4
   - Rationale: numbers with >4 divisors can never satisfy the requirement, so further checks are wasteful

4. **Validation and accumulation**:
   - After scanning (or early termination), check if exactly 4 unique divisors exist
   - If valid, add the sum of all four divisors to the running total

5. **Return final sum**: After processing all numbers, return the accumulated total

## Time Complexity Analysis

- **Per-number complexity**: O(√n) in worst case (when scanning completes without early termination)
  - Early termination typically reduces actual work: most composite numbers exceed 4 divisors quickly
  - Perfect squares handled correctly without special cases due to set deduplication

- **Overall complexity**: O(N · √M)
  - `N` = length of input array
  - `M` = maximum value in the array
  - With constraints `M ≤ 10⁵`, √M ≤ 317 → practical upper bound of ~317 operations per number

- **Space complexity**: O(1) auxiliary space
  - Divisor set never holds more than 5 elements (due to early termination at size >4)
  - Constant space regardless of input size
