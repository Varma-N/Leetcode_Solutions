# 2751. Robot Collisions

### **Step-by-Step Approach**

**1. Bundle and Track Original Indices**
Because the final requirement is to return the surviving robots' healths in the *exact order they were provided in the input*, the arrays cannot be sorted directly. The first step is to create a combined list where each element groups a robot's position, health, direction, and original index.

**2. Sort by Position**
Once the data is bundled, sort the robots by their position. This allows the simulation to process chronologically from left to right, matching their physical layout on the line.

**3. Initialize Tracking Structures**
Two primary containers are needed:
* **Stack:** To hold robots moving Right (`R`). These robots act as a buffer, waiting to see if they crash into any left-moving robots ahead of them.
* **Survivors List:** To hold robots moving Left (`L`) that successfully clear all obstacles, as well as the final surviving right-moving robots.

**4. Process the Robots (Left to Right)**
Iterate through the sorted list of robots one by one:
* **Right-Moving Robots (`R`):** Push them directly onto the stack. They cannot collide with anything behind them and must wait to see what is ahead.
* **Left-Moving Robots (`L`):** This triggers a potential collision phase. This robot must be evaluated against the top of the stack (which contains the right-moving robots it is about to crash into).

**5. Resolve Collisions (The Fight Phase)**
While there are right-moving robots in the stack and the current left-moving robot is still alive (health > 0), they crash. Compare their health values:
* **The Stacked (`R`) robot is stronger:** The `R` robot takes 1 point of damage. The `L` robot dies (health becomes 0). The collision loop ends.
* **The Current (`L`) robot is stronger:** The `L` robot takes 1 point of damage. The `R` robot dies (pop it from the stack). The collision loop continues because the `L` robot keeps moving and might hit the next robot in the stack.
* **Both are equal:** Both robots die. Pop the `R` robot from the stack and set the `L` robot's health to 0. The collision loop ends.

**6. Store Survivors**
If the left-moving robot destroys everything in the stack (or if the stack was empty to begin with) and still has health remaining, append it to the Survivors List. It is now safe from any future collisions.

**7. Final Cleanup and Reordering**
Once the main iteration is complete, any right-moving robots still sitting in the stack have survived. Move them all into the Survivors List. Finally, sort the Survivors List based on the `original_idx` saved in Step 1, and map the array to extract just their health values for the final output.

---

### **Complexity Analysis**

* **Time Complexity:** **O(N log N)**
    * Grouping the arrays takes **O(N)** time.
    * Sorting the array by position takes **O(N log N)** time.
    * Processing the robots takes **O(N)** time. Even though there is a `while` loop nested inside the `for` loop, each right-moving robot is pushed to the stack exactly once and popped at most once. 
    * Sorting the survivors back to their original order takes **O(N log N)** time in the worst-case scenario.
    * Therefore, the sorting operations heavily dominate the overall time complexity.

* **Space Complexity:** **O(N)**
    * Creating the bundled `robots` array requires **O(N)** space.
    * The `stack` and the `survivors` list will also hold up to **N** elements combined in the worst-case scenario (e.g., when all robots move in the same direction and zero collisions occur).
