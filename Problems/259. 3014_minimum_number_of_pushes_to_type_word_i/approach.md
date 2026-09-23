# Problem 3014: Minimum Number of Pushes to Type Word I

## Intuition
The core idea is to determine the minimum number of pushes required to type the given word using a remapped telephone keypad.  We can achieve this by leveraging the following:

* **Mapping of Keys:** The task can be simplified by understanding the mapping between the keys and the letters.
* **Remapping:** The key is to remap the keys, to optimize for the minimum number of pushes. 


## Approach

1. **Character Analysis:** Analyze the word and map the letters to keys, considering how each letter is mapped to a specific key on the phone keypad.  
    * We can utilize the following for our mapping: 
        *  Example 1: The key mapping can be represented as a table of how each letter maps to a specific key. 
    * For Example 2: a mapping can be represented as a table of how each letter maps to a specific key.  
    
2. **Remapping:** We will use a table to represent how the keys are mapped to letters.
    *  For Example 1: This table would be structured to show the mapping for each letter (e.g., a = 2, b = 3, c = 4, etc.).  
    *  For Example 2: This table would be structured to show the mapping for each letter (e.g., a = 2, b = 3, c = 4, etc.).  

3. **Calculating the Minimum Pushes:**  Once the remapping is complete, we need to determine the minimum number of pushes to type the word.  This can be achieved by utilizing a table to show the mapping for each letter and then applying a sum operation.


## Complexity Analysis

* **Time Complexity:** $O(N)$
    * The time complexity is determined by the number of iterations required to analyze the input.  We will be iterating through the input string.  
* **Space Complexity:** $O(1)$
    * The space complexity is constant, as we are not creating any new data structures.  We will just be using a table to map the keys to the letters.
