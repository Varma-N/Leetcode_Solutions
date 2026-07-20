```markdown
# Problem 3120: Count the Number of Special Characters I

## Intuition
A special character is any letter that appears both as a lowercase and uppercase instance in the input string.  We can leverage this fact to identify and count these characters efficiently by comparing each individual letter with its corresponding uppercase counterpart. 


## Approach
1. **Initialization:** We begin by creating a set named `seen` containing all the unique letters present within the input string `word`. This ensures that we avoid redundant checks for already seen letters. 

2. **Iteration and Comparison:** Next, we iterate through the `seen` set using a loop.  For each letter (`i`) in `seen`,  we check if its uppercase counterpart exists as well in the `seen` set.
   * If both the lowercase and uppercase versions of the letter exist in the `seen` set, indicating that it is a special character, we append this letter (converted to lower case) into our `res` set.

3. **Count:** After processing all letters within the input string, we return the length of `res`. The length of the result set reflects the number of special characters found in the word. 


## Complexity Analysis
* **Time Complexity:** $O(N)$  where N is the length of the input string `word`. This complexity arises from iterating through each character and checking its uppercase counterpart once during our algorithm execution.
    * [Detailed explanation of why]  
* **Space Complexity:** $O(1)$  The algorithm utilizes a set to store unique letters encountered, leading to a constant space complexity. 
    * [Detailed explanation of why]