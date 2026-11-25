# Problem 20: Valid Parentheses

## Intuition
The core idea is to implement a stack-based approach to validate the parentheses. We maintain a stack to store open brackets and compare them with the closing brackets. If we encounter a closing bracket, we must have an open bracket to match.  We continue to the next bracket until all brackets are closed. 

## Approach
1. **Initialization:**
   -  A dictionary `parentheses_dict` is created to map each opening bracket to its corresponding closing bracket (e.g., `'('` to `')'`).
   -  An empty stack `stack` is initialized to store the open brackets encountered.

2. **Iterating through the string `s`:**
   -  For each character `i` in the string `s`:
     -   **If `i` is an opening bracket:** Push `i` onto the stack. 
     -   **If `i` is a closing bracket:** 
        -  **Check if the stack is not empty and the top element is a matching opening bracket:** If so, pop the top element from the stack as a match is found.
        -  **If the stack is empty or the top element doesn't match the current closing bracket:** Return `False`, as there's no matching opening bracket. 

3. **Final Check:**
   -  After processing the entire string, if the stack is empty, then all the open brackets have been matched with their corresponding closing brackets. Return `True`. Otherwise, return `False`.


## Complexity Analysis
* **Time Complexity:** $O(N)$ 
    -  The algorithm iterates through the string `s` once. 
* **Space Complexity:** $O(N)$ 
    -  The stack stores a maximum of `N` elements (the length of the input string).