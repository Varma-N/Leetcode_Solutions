# 1266. Minimum Time Visiting All Points 

## Intuition
From one point to the next, you can move:
- 1 unit horizontally,
- 1 unit vertically, or
- 1 unit diagonally  
in **1 second**.

A diagonal move reduces both the x-distance and y-distance by 1 at the same time.  
So, to minimize time, we should use as many diagonal moves as possible.

---

## Step-by-Step Approach

1. Initialize `total_time = 0`.
2. Iterate through the list of points from the second point to the last.
3. For each consecutive pair of points:
   - Let the previous point be `(x1, y1)`
   - Let the current point be `(x2, y2)`
4. Compute:
   - Horizontal distance = `abs(x2 - x1)`
   - Vertical distance = `abs(y2 - y1)`
5. The minimum time to move between these two points is:
`max(horizontal distance, vertical distance)`
because diagonal moves can cover both directions simultaneously.
6. Add this value to `total_time`.
7. After processing all points, return `total_time`.

---

## Why This Works
- Diagonal moves are optimal until one direction is exhausted.
- Any remaining distance must be covered by straight moves.
- Therefore, the total time is determined by the larger of the two distances.

---

## Time Complexity
- **O(n)**  
where `n` is the number of points.  
We process each consecutive pair once.

---

## Space Complexity
- **O(1)**  
Only a constant amount of extra space is used.

---
