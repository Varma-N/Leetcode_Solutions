# Problem 1872: Stone Game VIII

## Intuition
The solution utilizes dynamic programming to determine the optimal score difference between Alice and Bob during the Stone Game.  The core idea is to calculate the score difference based on the sum of the values of the stones after each player takes their turn.  We track the score difference between Alice and Bob by iteratively updating a `dp` variable.  The `dp` variable stores the current largest score difference, with the game ending when only one stone remains in the row.


## Approach
1.  **Calculate Stone Value:**  The code calculates the sum of the stones by iterating through the `stones` array and adding the value of the current stone to the previous stone's value.
2. **Dynamic Programming:** The code iterates through the `stones` array from the second-to-last element (index `len(stones) - 2`) to the first element (index `0`), calculating the score difference at each step. 

**Note:** The `dp` variable is initially set to the last stone's value (`stones[-1]`).  We then iterate backwards through the array and update `dp` whenever the difference between the current stone's value (`stones[i]`) and the previous `dp` value is greater. 
 
 


## Complexity Analysis
* **Time Complexity:** $O(N)$
    *  The code iterates through the `stones` array once. The time complexity is determined by the nested loop.
* **Space Complexity:** $O(1)$ 
    * The time complexity is $O(N)$ as we have to traverse through the array.