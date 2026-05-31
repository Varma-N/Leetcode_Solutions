# Approach: Walking Robot Simulation II

## Step-by-Step Approach

1.  **Grid Flattening and Perimeter Calculation:**
    Instead of treating the grid as a 2D matrix, realize that the robot only walks along the outer edges. This turns the path into a 1D loop.
    Calculate the total perimeter: `perimeter = 2 * (width + height - 2)`.

2.  **State Initialization (`__init__`):**
    * Store the `width` and `height`.
    * Initialize the linear position `pos = 0`.
    * Maintain a boolean flag `moved = False`. This is crucial because the starting direction at `(0, 0)` is "East", but if the robot completes a full circuit and returns to `(0, 0)`, it will be facing "South".

3.  **Optimized Movement (`step`):**
    * Mark `moved = True` since a step is being taken.
    * Instead of simulating step-by-step (which would result in a Time Limit Exceeded error for large `num`), update the position using modulo arithmetic: `pos = (pos + num) % perimeter`. This instantly skips any redundant full loops around the grid.

4.  **Coordinate Mapping (`getPos`):**
    To find the `(x, y)` coordinates from the linear `pos`, map the position to one of the four edges:
    * **Bottom Edge (Moving East):** If `pos < width`, the coordinates are `(pos, 0)`.
    * **Right Edge (Moving North):** If `pos < width + height - 1`, the coordinates are `(width - 1, pos - (width - 1))`.
    * **Top Edge (Moving West):** If `pos < 2 * width + height - 2`, the coordinates are `(width - 1 - (pos - (width + height - 2)), height - 1)`.
    * **Left Edge (Moving South):** For the remaining positions, the robot is on the left edge moving down: `(0, height - 1 - (pos - (2 * width + height - 3)))`.

5.  **Direction Mapping (`getDir`):**
    Determine the facing direction based on the segment the current `pos` falls into:
    * If `pos == 0`: Return "South" if `moved` is true, otherwise "East".
    * **Bottom segment (`0 < pos < width`):** Return "East".
    * **Right segment (`width <= pos < width + height - 1`):** Return "North".
    * **Top segment (`width + height - 1 <= pos < 2 * width + height - 2`):** Return "West".
    * **Left segment:** Return "South".

---

## Complexity Analysis

* **Time Complexity:** * `__init__(width, height)`: $\mathcal{O}(1)$
    * `step(num)`: $\mathcal{O}(1)$ - Constant time due to the use of the modulo operator, avoiding step-by-step loops.
    * `getPos()`: $\mathcal{O}(1)$ - Simple arithmetic boundary checks.
    * `getDir()`: $\mathcal{O}(1)$ - Simple conditional checks.
    * **Overall Time Complexity: $\mathcal{O}(1)$** per method call.

* **Space Complexity:** * **$\mathcal{O}(1)$** - The robot's state only requires storing a few scalar variables (`width`, `height`, `pos`, `perimeter`, `moved`). No extra space scaling with grid size or step count is used.
