# Problem 1190: Reverse Substrings Between Each Pair of Parentheses

## Intuition
The key idea is to utilize a stack to track the order of substrings that need to be reversed. We iterate through the string, and for every '(' we push the current string to the stack, indicating a new substring begins. For every ')' we pop the stack, and reverse the remaining substring using slicing (`current_string[::-1]`). 

## Approach
1. **Initialization:** 
    * `res = []`: An empty list to store the final result.
    * `stack = []`: An empty stack to keep track of the order of substrings.
    * `current_string = ""`: A string to store the currently active substring.

2. **Iterating through the String:**
    *  For each character (`ch`) in the string `s`:
        * **If `ch` is '(':**
            * Push the `current_string` to the `stack`. This indicates the start of a new substring.
            * Reset `current_string` to an empty string.
        * **If `ch` is ')':**
            * Pop the top element from the `stack`. This retrieves the previous substring to be reversed.
            *  Reverse the substring using slicing: `current_string = temp + current_string[::-1]` 
        * **Else (non-bracket):**
            * Append the character to the `current_string`.

3. **Result Building:** After iterating through the entire string, the `current_string` will hold the complete reversed string, so return this string to the program.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the string `s` once. The operations inside the loop are also linear in time, making the overall time complexity $O(N)$.
* **Space Complexity:** $O(N)$
    * The `stack` stores the order of substrings, and the `res` list stores the final reversed result. The `current_string` variable may grow in size, but its maximum growth is proportional to the length of the input string.