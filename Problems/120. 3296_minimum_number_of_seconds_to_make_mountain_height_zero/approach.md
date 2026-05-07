# Approach: Minimum Seconds to Reduce Mountain Height

To find the minimum time required for workers to reduce the mountain height to zero, we use a binary search on the total time elapsed.

### Step-by-Step Approach

1.  **Identify the Search Space**:
    *   The minimum possible time is **0** (if the height is already 0).
    *   A safe upper bound is the time it would take the fastest worker to reduce the entire mountain alone. If the fastest worker has base time $W$ and the height is $H$, the time taken is $W \cdot \frac{H(H+1)}{2}$.

2.  **Binary Search for Minimum Time**:
    *   Perform a binary search within the range `[0, upper_bound]`.
    *   For each `mid` time value, determine if all workers combined can reduce a height of at least `mountainHeight`.

3.  **Feasibility Check (`can_finish` function)**:
    *   For a given total time $T$, calculate the maximum height $x$ each worker $i$ with base time $w_i$ can contribute.
    *   The formula for time taken by a worker to reduce height $x$ is:
        $$Time = w_i \cdot \frac{x(x + 1)}{2}$$
    *   To find the maximum $x$ for a fixed $T$, solve the inequality:
        $$w_i \cdot \frac{x^2 + x}{2} \leq T \implies x^2 + x - \frac{2T}{w_i} \leq 0$$
    *   Using the quadratic formula, the maximum integer $x$ is:
        $$x = \left\lfloor \frac{-1 + \sqrt{1 + \frac{8T}{w_i}}}{2} \right\rfloor$$
    *   Sum the $x$ values for all workers. If the total sum $\geq mountainHeight$, the time $T$ is feasible.

4.  **Optimize the Search**:
    *   Sort the worker base times initially.
    *   During the feasibility check, if the running sum of heights reaches `mountainHeight`, return `True` immediately to save cycles.

5.  **Final Result**:
    *   Adjust the binary search boundaries based on the feasibility check until the minimum possible time is narrowed down.

### Complexity Analysis
*   **Time Complexity**: O(N log(MaxTime)) where N is the number of workers. Sorting the workers takes O(N log N).
*   **Space Complexity**: O(1) as no extra data structures are required beyond input storage.
