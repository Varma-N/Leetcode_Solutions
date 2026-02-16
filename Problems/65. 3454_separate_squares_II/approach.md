# 3454. Separate Squares II

## 📋 Problem Overview
Given a list of squares on a 2D plane (defined by bottom-left x, y and side length `l`), find the **y-coordinate** of a horizontal line that divides the **total union area** of all squares into two equal halves.

> **Key Challenge**: Squares may overlap. We must calculate the area of the *union* of shapes, not the sum of individual areas.

---

## 🎯 Key Insights
1. **Union Area Calculation**: Simple summation fails due to overlaps. We need a way to track active coverage at any height.
2. **Sweep Line Algorithm**: By sweeping a horizontal line from bottom to top, we can process changes in geometry only at specific y-coordinates (square bottoms and tops).
3. **Segment Tree**: Used to efficiently maintain the total length of the union of active x-intervals as we sweep. This allows $O(\log N)$ updates and queries.
4. **Two-Pass Approach**:
   - **Pass 1**: Calculate the total union area.
   - **Pass 2**: Sweep again to find the exact y-coordinate where the accumulated area reaches half of the total.

---

## 📝 Step-by-Step Approach

### Step 1: Event Creation
For every square `(x, y, l)`:
- Create a **Start Event** at `y` (type `+1`) covering interval `[x, x+l]`.
- Create an **End Event** at `y+l` (type `-1`) covering interval `[x, x+l]`.
- Collect all unique x-coordinates to build a coordinate compression map.

### Step 2: Coordinate Compression
Since x-coordinates can be large or non-integer, map all unique x-values to indices `0..N`. The segment tree will operate on these indices representing intervals between consecutive x-values.

### Step 3: Segment Tree Logic
The tree maintains two arrays:
- `cnt[node]`: How many active squares fully cover this node's range.
- `length[node]`: The actual covered length in this node's range.

**Push Up Logic**:
- If `cnt[node] > 0`: The entire range is covered. `length = xs[r] - xs[l]`.
- If `cnt[node] == 0`: The coverage is the sum of children's coverage (`length[left] + length[right]`).

### Step 4: First Sweep (Total Area)
1. Sort events by y-coordinate.
2. Iterate through events. For each gap between `prev_y` and current `y`:
   - Add `current_covered_length * (y - prev_y)` to `total_area`.
   - Update the segment tree with the current event (add or remove interval).
   - Update `prev_y`.

### Step 5: Second Sweep (Find Split Line)
1. Reset the segment tree and accumulators.
2. Target area = `total_area / 2`.
3. Iterate through events again:
   - Calculate area of the current strip: `chunk = current_covered_length * (y - prev_y)`.
   - If `current_accumulated_area + chunk >= target`:
     - The split line lies within this strip.
     - Calculate exact offset: `needed = target - current_accumulated_area`.
     - Result: `prev_y + (needed / current_covered_length)`.
   - Otherwise, add chunk to accumulator, update tree, and continue.

---

## 🔄 Visual Example

**Input**: Two overlapping squares.
1. Square A: `(0, 0, 2)` → Area 4
2. Square B: `(1, 1, 2)` → Area 4
   - Overlap region: `(1, 1)` to `(2, 2)` → Area 1
   - **Union Area**: $4 + 4 - 1 = 7$. **Target**: $3.5$.

**Sweep Process**:
| Y Range | Active X Intervals | Covered Length | Strip Height | Strip Area | Cumulative Area |
| - | - | - | - | - | - |
| 0 → 1 | `[0, 2]` | 2 | 1 | 2.0 | 2.0 |
| 1 → 2 | `[0, 3]` (Union of A&B) | 3 | 1 | 3.0 | 5.0 |
| 2 → 3 | `[1, 3]` | 2 | 1 | 2.0 | 7.0 |

**Finding Split**:
- At $y=1$, cumulative is $2.0$ (Need $1.5$ more).
- Next strip ($y=1 \to 2$) has length $3$.
- Required height: $1.5 / 3 = 0.5$.
- **Result**: $y = 1 + 0.5 = 1.5$.

---
## ⏱️ Complexity Analysis

### Time Complexity: $O(N \log N)$
- **Sorting Events**: There are $2N$ events (2 per square). Sorting takes $O(N \log N)$.
- **Coordinate Compression**: Sorting unique x-coordinates takes $O(N \log N)$.
- **Sweep Loop**: We iterate through $2N$ events.
- **Segment Tree Operations**: Each `update` takes $O(\log N)$ time.
- **Total**: $O(N \log N) + O(N \log N) = O(N \log N)$.

### Space Complexity: $O(N)$
- **Events & Coordinates**: Storing events and unique x-coordinates requires $O(N)$ space.
- **Segment Tree**: The tree array size is proportional to the number of unique x-coordinates, i.e., $O(N)$.
- **Total**: $O(N)$.
    
