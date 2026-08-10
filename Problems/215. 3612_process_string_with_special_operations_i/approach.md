# Problem 3612: Process String with Special Operations I

## Intuition
The core idea is to use a stack-based approach to process the string `s`. We can track the current state by keeping a list of characters (`res`) and applying special operations such as '*' (removal), '#' (duplication) and '%' (reversal) using this stack. This allows us to efficiently manipulate the string according to the rules given in the problem statement.


## Approach
1. **Initialization:** 
    - Create an empty list `res` to store the processed characters.

2. **Iterating through the String:**
    - For each character `i` in the input string `s`: 
        - **Case: If `i` is an alphabetic character (using `isalpha()`):** Append `i` to the `res` list.
        - **Case: If `i` is '*' and  `res` is not empty:** Pop the last element from `res`, effectively removing it. 
        - **Case: If `i` is '#' :** Append the content of `res` by itself, effectively duplicating the current result.
        - **Case: If `i` is '%' :** Reverse the content of `res` using the reverse operation.

3. **Returning the Result:** 
    - Join all characters in `res` into a single string using `''.join(res)` and return it as the final processed string.


## Complexity Analysis
* **Time Complexity:** $O(N)$ where N is the length of the input string. We iterate through each character once.
   * This complexity is achieved because we visit each character in the string exactly once. 
* **Space Complexity:** $O(1)$. The algorithm uses a constant amount of extra space, regardless of the input size.