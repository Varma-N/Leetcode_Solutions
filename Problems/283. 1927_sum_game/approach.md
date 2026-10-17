# Problem 1927: Sum Game

## Intuition
The solution exploits the cyclical nature of the game to determine the winning player.  This is done by analyzing the sum of the digits in both the left and right halves of the string. 

If the sums of the left and right halves are not equal, the game is won by Alice, and if they are equal, the game is won by Bob.

## Approach
1. **Initialization:** 
   - Determine the length of the input string (`n`).
   - Calculate the middle index (`mid`) of the string.
   - Initialize two variables, `s_l` and `s_r`, for storing the sum of digits in the left and right halves respectively.
   - Initialize two variables, `q_l` and `q_r`, for tracking the number of '?' characters in the left and right halves. 


2. **Left Half Analysis:** 
   - Loop through the left half of the string (`range(mid)`).
   - If a character is a '?' character, increment `q_l`.
   - Otherwise, add the digit value of the current character to `s_l`. 

3. **Right Half Analysis:**
   - Loop through the right half of the string from `mid` onwards. 
   - If a character is a '?' character, increment `q_r`.
   - Otherwise, add the digit value of the current character to `s_r`. 

4. **Determining the Winner:**
   - Check if the sum of '?' characters in the left and right halves (`q_l + q_r`) is odd. 
   - If odd, return `True` to indicate Alice wins. 
   - Otherwise, check if the difference between `s_l` and `s_r` is equal to 9 times the difference between `q_r` and `q_l` divided by 2. 
   - If true, return `True`, if false, return `False`

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The code iterates through the string twice.
* **Space Complexity:** $O(1)$
    * The time complexity is dominated by the number of characters in the string.