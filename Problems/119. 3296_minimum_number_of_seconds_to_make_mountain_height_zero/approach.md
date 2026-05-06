# Minimum Number of Seconds to Make Mountain Height Zero - Logic & Approach

## Step-by-Step Approach

1.  **Identify the Monotonic Property**:
    The problem asks for the *minimum* time. Since the ability to finish the task in time `T` implies we can also finish it in any time greater than `T`, the search space for time is monotonic. This makes the problem ideal for **Binary Search on the Answer**.

2.  **Define the Search Range**:
    - **Lower Bound (`low`)**: 1 second.
    - **Upper Bound (`high`)**: The time it would take the fastest worker (minimum `workerTime`) to reduce the entire `mountainHeight` alone. This is calculated using the sum of the first `H` multiples of `w`: $w \cdot rac{H(H+1)}{2}$.

3.  **Implement the Feasibility Check (`can_finish`)**:
    For a candidate `time` $T$, determine if the total reduction by all workers $\ge mountainHeight$.
    - For each worker with base time $w$, find the maximum $x$ such that:
      $w \cdot rac{x(x+1)}{2} \le T$
    - This simplifies to a quadratic inequality: $x^2 + x - rac{2T}{w} \le 0$.
    - Solve for $x$ using the quadratic formula: $x = \lfloor rac{-1 + \sqrt{1 + rac{8T}{w}}}{2} 
floor$.
    - Sum the $x$ values for all workers. If the sum reaches `mountainHeight`, the time is feasible.

4.  **Optimization**:
    - Sort the `workerTimes` array. This allows the `can_finish` function to reach the `mountainHeight` threshold faster and return `True` early.
    - Use integer square root (`math.isqrt`) for precise and efficient calculation of the quadratic root.

5.  **Binary Search Execution**:
    - If `can_finish(mid)` is true, update the result and try a smaller value (`high = mid - 1`).
    - Otherwise, try a larger value (`low = mid + 1`).

## Complexity Analysis

### Time Complexity
- **Sorting**: $O(W \log W)$, where $W$ is the number of workers.
- **Binary Search**: $O(W \cdot \log(	ext{max\_time}))$.
  - The `max_time` is roughly $10^6 \cdot rac{10^5 \cdot 10^5}{2}  pprox 5 \cdot 10^{15}$.
  - $\log_2(5 \cdot 10^{15})  pprox 52$.
  - For each step of binary search, we iterate through $W$ workers.
- **Total**: $O(W \cdot (\log W + \log(	ext{max\_time})))$.

### Space Complexity
- **Space**: $O(1)$ (ignoring the space used by the sorting algorithm, which is typically O(W) or O(log W).
