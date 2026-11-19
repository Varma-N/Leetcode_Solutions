# Problem 1096: Brace Expansion II

## Intuition
The key idea is to break down the input expression recursively into smaller sub-expressions, then expand those sub-expressions using the defined grammar rules.  We start by finding the outermost opening bracket, followed by the innermost opening bracket.  The sub-expressions are then recursively expanded using the defined grammar rules.  We then use a set to keep track of the unique words that are found.


## Approach
1. **Find the Opening Bracket**: Locate the index of the outermost opening bracket '{' within the input expression. This index marks the start of the sub-expression.
2. **Find the Innermost Bracket**:  Locate the index of the innermost opening bracket '{' within the sub-expression, which is the boundary for the current level of recursion.
3. **Split by Commas**: Split the sub-expression string by commas ',' into individual expressions. This provides each word's expression in its own sub-expression.
4. **Recursive Expansion**: Recursively call the `braceExpansionII` function for each sub-expression.
5. **Sort and Return**: After all sub-expressions have been evaluated, the unique words are collected in a set and sorted in alphabetical order.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * The recursive calls explore the input expression until all sub-expressions are expanded.  
* **Space Complexity:** $O(N)$
    * The set used to store the words is used in a space-efficient manner.