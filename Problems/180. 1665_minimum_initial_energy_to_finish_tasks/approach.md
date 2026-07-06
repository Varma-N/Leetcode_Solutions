# Problem 1665: Minimum Initial Energy to Finish Tasks

## Intuition
The problem asks us to determine the minimum initial energy required to complete a series of tasks, given their actual and minimum energy requirements. We can achieve this by sorting the tasks based on their minimum energy requirement and then progressively reducing our energy level as we complete each task. The key is using the `min` function to efficiently check for a valid task start.

## Approach
1. **Sort Tasks:**
   - Sort the `tasks` array (input) in descending order based on the `minimum` value of the tasks ([minimum, actual]). This prioritizes tasks with higher minimum energy requirements to be finished first and thus lower initial energy requirement. 

2. **Initialization:**
   - Initialize `total_initial` to 0: This variable will store the total initial energy required to start all tasks.
   - Initialize `current_energy` to 0: This represents your current energy level for task execution.

3. **Iterating Through Tasks:**
   - Loop through each `actual`, `minimum` pair in the sorted `tasks` array. 
   - **Check for Feasibility:**  
     - If the `current_energy` is less than the `minimum` requirement: 
        - Calculate the "shortfall" (the amount of energy needed to reach the minimum) 
        - Add this `shortfall` to `total_initial`, as it's needed for starting the task
        - Increase `current_energy` by `shortfall` to account for initial energy expenditure.

4. **Task Completion:**
   - Subtract the actual energy spent (`actual`) from `current_energy` in each iteration. This reflects energy decrease after completing a task. 


## Complexity Analysis
* **Time Complexity:** $O(N log N)$
    * Sorting the tasks takes O(N log N) time complexity using a merge sort or quick sort algorithm. 
* **Space Complexity:** $O(1)$
    * The solution uses a constant amount of extra space, independent of input size.