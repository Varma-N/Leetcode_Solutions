# Problem 1111: Maximum Nesting Depth of Two Valid Parentheses Strings

## Intuition
[A valid parentheses string consists of "(" and ")" characters only. The goal is to split a VPS into two subsequences such that the maximum nesting depth of either subsequence is minimized. This can be achieved by strategically splitting the VPS based on its structure.]

## Approach
1. **Initialization:**
   - `res`: An empty list to store the result array.
   - `level`: A variable to track the current nesting depth, initialized to 0.

2. **Iterate through the input string `seq`:**
   - For each character `i` in the string:
     - If `i` is an opening parenthesis "(":
       - Append the current `level` (the current depth) to the `res` list (0 to indicate membership in A).
       - Increment the `level` by 1 to represent moving into a deeper nesting level.
     - If `i` is a closing parenthesis ")":
       - Decrement the `level` by 1 to move back to a shallower nesting level.
       - Append the updated `level` to the `res` list.

3. **Return the result array `res`:**
   - The `res` array will now contain the membership of each character in the subsequences A and B.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The algorithm iterates through the string `seq` once to process each character.
* **Space Complexity:** $O(1)$
    * The algorithm uses a constant amount of extra space for variables.