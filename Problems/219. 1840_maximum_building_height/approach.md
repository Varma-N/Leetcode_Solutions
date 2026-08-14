# Problem 1840: Maximum Building Height

## Intuition
To find the maximum building height in a city with given restrictions, we need to strategically place buildings while ensuring they meet the height limitations and avoid violating the adjacent building constraint. We can utilize dynamic programming by considering the heights of each building and their neighboring buildings and storing the result for each position.  This allows us to quickly calculate the height of each building at every stage without recalculating it from scratch.

## Approach
We will use a dynamic programming approach to solve this problem. 

1. **Initialization:**
    - We first append [1, 0] to the `restrictions` array to handle the special case where the first building needs height 0 and satisfies the adjacent building constraint. 
    - We sort the `restrictions` array based on increasing 'idi' (building ID).  

2. **Iterative Calculation:**
   - For each position in the sorted `restrictions` array, we calculate the minimum allowable height for that building (`min(restrictions[i][1], restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0])`)

3. **Calculating Final Maximum Height:**
  - We iterate through the sorted `restrictions` array, starting from the second-to-last element, and calculate the maximum height possible by considering the heights of adjacent buildings (`(h1 + h2 + id2 - id1) // 2`).
   - The final result is obtained as the sum of the maximum height of a building plus the remaining height of the last building.

  
## Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the `restrictions` array, performing a constant number of operations for each iteration. 


* **Space Complexity:** $O(1)$
   * We only use a constant amount of additional space to store our intermediate results and variables.