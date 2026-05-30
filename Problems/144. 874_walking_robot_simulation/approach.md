### Step-by-Step Approach

**1. Optimize Obstacle Lookup**
To efficiently check if the robot is about to step on an obstacle, convert the given list of obstacles into a hash set containing tuples of coordinates. This reduces the time complexity of checking for an obstacle from O(M) to O(1) for each step.

**2. Define Movement Directions**
Set up two arrays, `dx` and `dy`, to represent movement along the X and Y axes for the four cardinal directions. By ordering them clockwise (North, East, South, West), you can easily manage direction changes using mathematical modulo operations:
* Index 0 (North): `dx = 0`, `dy = 1`
* Index 1 (East): `dx = 1`, `dy = 0`
* Index 2 (South): `dx = 0`, `dy = -1`
* Index 3 (West): `dx = -1`, `dy = 0`

**3. Initialize State Variables**
Set up the starting conditions for the robot:
* `x` and `y` coordinates to `0` (starting at the origin).
* Direction index `di` to `0` (initially facing North).
* `max_sq_dist` to `0` to keep track of the maximum Euclidean distance squared from the origin.

**4. Process Each Command**
Iterate through the list of commands one by one and apply the corresponding logic:
* **Turning Left (Command -2):** Update the direction index using `(di + 3) % 4`. This correctly shifts the index counter-clockwise.
* **Turning Right (Command -1):** Update the direction index using `(di + 1) % 4`. This correctly shifts the index clockwise.
* **Moving Forward (Command > 0):** Iterate step-by-step for the given number of units. 
    * Calculate the tentative next coordinates `(nx, ny)` using the current position and the active direction from `dx` and `dy`.
    * Check if `(nx, ny)` exists in the `obstacle_set`.
    * If it is an obstacle, stop moving for the current command entirely and move on to the next command.
    * If the path is clear, update the current `x` and `y` coordinates.
    * Calculate the current squared distance from the origin (`x*x + y*y`) and update `max_sq_dist` if this new distance is greater than the previous maximum.

**5. Return the Result**
Once all commands have been processed, return `max_sq_dist` as the final answer.

---

### Complexity Analysis

* **Time Complexity:** **O(N + M)**
    * **M** is the number of obstacles. Converting the obstacle list to a hash set takes O(M) time.
    * **N** is the number of commands. The robot processes each command, and since the maximum number of steps per command is bounded by a constant (9), moving the robot takes at most 9 operations per command. Thus, processing commands takes O(N) time.
    * The total time complexity is O(N + M).

* **Space Complexity:** **O(M)**
    * **M** is the number of obstacles. The hash set `obstacle_set` stores each obstacle as a tuple, requiring O(M) extra space. Variables and direction arrays require constant O(1) space.
