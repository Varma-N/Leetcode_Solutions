# Problem 2463: Minimum Total Distance Traveled

## Approach

### Step-by-Step Breakdown

1.  **Preparation and Sorting:**
    * Sort both the `robot` positions and the `factory` positions in ascending order. Sorting ensures that we can make optimal assignment decisions greedily relative to the spatial arrangement.
2.  **Flatten Factory Constraints:**
    * Since each factory has a specific capacity limit, transform the `factory` input into a flattened list (`factory_positions`) where each factory location is repeated according to its capacity limit. This simplifies the problem into matching each robot to a specific "factory slot."
3.  **Dynamic Programming Table Initialization:**
    * Define a 2D DP table `dp[n + 1][m + 1]`, where `n` is the number of robots and `m` is the total capacity of all factories.
    * `dp[i][j]` represents the minimum total distance to assign robots from index `i` through `n-1` using factory slots from index `j` through `m-1`.
    * Initialize the base cases: if all robots are assigned (`i == n`), the cost is 0. If no factory slots remain but robots are still waiting (`j == m`), the cost is infinity (impossible state).
4.  **State Transition:**
    * For each robot `i` and factory slot `j`, we have two choices:
        * **Skip:** Don't assign robot `i` to factory slot `j`. Move to the next slot: `dp[i][j + 1]`.
        * **Take:** Assign robot `i` to factory slot `j`. Add the distance `abs(robot[i] - factory_positions[j])` to the result of assigning the remaining robots to the remaining slots: `abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]`.
    * The state value is the minimum of these two choices: `dp[i][j] = min(skip, take)`.
5.  **Final Result:**
    * The value at `dp[0][0]` provides the minimum total distance to assign all robots to available factory slots.

## Complexity Analysis

* **Time Complexity:** $O(N \cdot M)$
    * Where $N$ is the number of robots and $M$ is the total capacity of all factories. The solution fills a table of size $(N+1) \times (M+1)$, where each cell computation takes $O(1)$ time. Sorting the input arrays takes $O(N \log N + F \log F)$ (where $F$ is the number of factories), which is dominated by the DP process for large inputs.
* **Space Complexity:** $O(N \cdot M)$
    * We utilize a 2D array of size $(N+1) \times (M+1)$ to store the intermediate results of the subproblems.
