# Longest Balanced Subarray II - Approach

## Problem Understanding
Find the length of the longest subarray where the subarray is considered "balanced" based on parity contributions of elements, with the constraint that only the most recent occurrence of each unique value contributes to the balance calculation.

## Step-by-Step Approach

### Step 1: Parity-Based Value Transformation
- Convert each element in the array to a parity-based contribution:
  - `+1` if the number is even
  - `-1` if the number is odd
- This transformation allows us to track the net "balance" of even vs odd contributions.

### Step 2: Track Most Recent Occurrences
- Maintain a hash map `prev_index` that stores the last seen index for each unique value.
- **Key Insight**: For any value that appears multiple times, only its **most recent occurrence** should contribute to the current balance calculation. Earlier occurrences must have their contributions canceled out.

### Step 3: Efficient Range Updates with Segment Tree
- Use a **Segment Tree with Lazy Propagation** to maintain balance values across indices efficiently.
- For each index `i` processing value `nums[i]`:
  1. **Cancel previous contribution**: If `nums[i]` was seen before at index `prev`, update range `[0, prev]` by `-val` to remove the old contribution.
  2. **Add new contribution**: Update range `[0, i]` by `+val` to include the current occurrence's contribution.
  3. **Update tracking**: Set `prev_index[nums[i]] = i` to record the new most recent position.
- This ensures that at any point, the balance at index `j` represents the cumulative contribution of only the most recent occurrences of values up to position `j`.

### Step 4: Find Valid Balanced Subarrays
- After processing each index `i`, query the segment tree to find the **leftmost index** where the balance equals `0`.
- If such an index `left` exists where `left <= i`, then the subarray `[left, i]` has a net balance of `0`, meaning it is balanced.
- Track the maximum length: `max_len = max(max_len, i - left + 1)`.

### Step 5: Optimized Zero-Balance Search with Pruning
- Enhance the segment tree query with **pruning logic**:
  - Each node stores both `min_balance` and `max_balance` for its segment.
  - If `min_balance > 0` or `max_balance < 0` for a segment, zero cannot exist in that segment—skip it entirely.
  - This reduces unnecessary traversal and achieves efficient `O(log n)` amortized query time.
- Recursively search left child first to find the leftmost valid index, ensuring we get the longest possible subarray.

### Step 6: Lazy Propagation for Efficiency
- Implement lazy propagation in the segment tree to defer range updates.
- When updating a range, mark child nodes with pending updates instead of immediately propagating, reducing redundant operations.
- Apply pending updates only when necessary during queries or further updates.

## Time and Space Complexity

| Complexity | Analysis |
|------------|----------|
| **Time** | `O(n log n)` - Process each of `n` elements once; each segment tree update and query takes `O(log n)`; pruning ensures efficient zero-balance search |
| **Space** | `O(n)` - Segment tree uses `O(4n) = O(n)` space; hash map for tracking previous indices uses `O(n)` space in worst case |
