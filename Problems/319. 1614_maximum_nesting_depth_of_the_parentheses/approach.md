```markdown
# Problem 1614: Maximum Nesting Depth of the Parentheses

## Intuition
Given a string `s` containing only parentheses, we need to find the maximum nesting depth of the parentheses. The maximum nesting depth means the maximum number of nested parentheses. We can achieve this by iterating through the string and incrementing a counter whenever we encounter an opening parenthesis and decrementing the counter whenever we encounter a closing parenthesis. The final count will be the maximum nesting depth.


## Approach
1. **Initialization:**
   -  `max_count`: variable to keep track of the maximum nesting depth, initialized to 0.
   -  `current_count`: variable to keep track of the current nesting depth, initialized to 0.

2. **Iteration:**
   -  Iterate through each character `char` in the string `s`.
   -  **If `char` is an opening parenthesis `(`:**
      - Increment `current_count` by 1.
      - If `current_count` exceeds `max_count`, update `max_count` to `current_count`.
   -  **If `char` is a closing parenthesis `)`:**
      - Decrement `current_count` by 1.

3. **Result:** Return the `max_count`, which represents the maximum nesting depth.


## Complexity Analysis
* **Time Complexity:** $O(N)$ where N is the length of the string. We iterate through the string only once.
* **Space Complexity:** $O(1)$  We use only a constant amount of space, regardless of the input size. 

``` 
```