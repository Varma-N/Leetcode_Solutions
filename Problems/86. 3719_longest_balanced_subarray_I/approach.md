# Longest Balanced Subarray - Approach

## Problem Understanding
Find the length of the longest contiguous subarray where the **count of distinct even numbers** equals the **count of distinct odd numbers**.

> Example: `[2, 3, 2, 3, 4]` → The subarray `[2, 3, 2, 3]` has 1 distinct even (2) and 1 distinct odd (3), so it's balanced with length 4.

---

## Core Intuition
For every possible starting position, expand the window to the right and track:
- Which **distinct** even numbers we've seen
- Which **distinct** odd numbers we've seen
- The **count** of each

When the counts match, we have a balanced subarray. Track the maximum length found.

---

## Step-by-Step Approach

### Step 1: Initialize Tracking Variables
- `best`: Stores the maximum balanced length found so far (start at 0)
- For each starting position, we'll need fresh trackers:
  - `seen_even`: Set to track distinct even values encountered
  - `seen_odd`: Set to track distinct odd values encountered
  - `cnt_even`: Counter for distinct even numbers (avoids repeated `len()` calls)
  - `cnt_odd`: Counter for distinct odd numbers

### Step 2: Outer Loop - Fix the Start Position
- Iterate through each index `i` as a potential starting point of a subarray
- **Early Termination Optimization**: If the remaining array length `(n - i)` cannot exceed the current `best`, break early. No need to check shorter possibilities.

### Step 3: Inner Loop - Expand the Window
- For each start position `i`, iterate `j` from `i` to the end of the array
- For each element `nums[j]`:
  1. **Classify**: Use bitwise check `(x & 1)` to determine if the number is odd or even
  2. **Track Distinct Values**: 
     - If the value hasn't been seen in its category, add it to the corresponding set and increment the counter
  3. **Check Balance**: If `cnt_even == cnt_odd`, calculate the current subarray length `(j - i + 1)` and update `best` if this is longer

### Step 4: Return the Result
- After checking all valid subarrays, return `best`

---

## Key Optimizations

| Optimization | Why It Helps |
|--------------|--------------|
| **Early Termination** | Skips unnecessary iterations when remaining length can't beat current best |
| **Bitwise Odd/Even Check** | `x & 1` is faster than `x % 2` for parity testing |
| **Explicit Counters** | Avoids repeated `len(set)` calls inside tight loop; O(1) counter update vs O(1) but with overhead |
| **Local Variable Hoisting** | `nums_local = nums` reduces attribute lookup overhead in Python loops |
| **Set for Distinct Tracking** | O(1) average-case lookup to check if a value was already counted |

---

## Why This Works
- **Exhaustive Search**: By checking every possible subarray, we guarantee finding the longest valid one
- **Distinct Tracking**: Sets ensure we only count unique values, not frequency
- **Balance Condition**: Explicit counter comparison directly implements the problem requirement

---

## Time Complexity
**O(n²)** where n is the length of the input array
- Outer loop runs O(n) times
- Inner loop runs O(n) times in worst case
- Set operations (add, lookup) are O(1) average case
- Early termination helps in practice but doesn't change worst-case complexity

## Space Complexity
**O(n)** in worst case
- `seen_even` and `seen_odd` sets can each store up to O(n) distinct values
- All other variables use O(1) space

---

## When to Use This Approach
✅ Small to medium input sizes (n ≤ 10³–10⁴)  
✅ When you need distinct value tracking  
✅ When early termination can prune significant search space  

❌ Very large inputs (n ≥ 10⁵) — consider sliding window or two-pointer optimizations if problem constraints allow
