# Problem 877: Stone Game

## Intuition
The key is understanding the game's rules. Alice or Bob can only take a single pile of stones at a time.  This implies we can analyze the game by strategically considering the initial pile that each player gets.

## Approach
1. **Initialization:** 
    * Create a `piles` list to hold the initial stone count for each pile.
    * Initialize a `player` variable to 1 (representing Alice, as she starts). 
    * Initialize a `current_sum` variable to 0.

2. **Determine the Winner:**
    * **Case 1:** If the current_sum is greater than 0, the current player wins. 
    * **Case 2:** If the current_sum is less than 0, the current player loses. 
    * **Case 3:** If the current_sum is 0, the game is a tie (no one wins). 
  
3. **Determine the next Player:**
    *  Assign the next player to the current player variable.  

4. **Loop:**
   *  Iterate through the piles list. 
   *  For each pile, the current player can either take the first or the last pile. 
   *  The `current_sum` is calculated. 
   *  The winner of the turn is determined and the game continues. 

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The algorithm iterates through the piles list once to determine the winner.  
* **Space Complexity:** $O(1)$
    * The algorithm only uses a few variables, and it does not need any additional storage.