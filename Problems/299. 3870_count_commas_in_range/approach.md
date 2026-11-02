# Problem 3870: Count Commas in Range

## Intuition
The core idea is to leverage the fact that commas are only inserted when there are three digits. We can use an efficient approach by breaking down the problem into smaller subproblems.

## Approach
1. **Initialization:** 
    - Create a variable `count` initialized to 0 to store the total count of commas.
    - Create a variable `n` initialized to `n` which will be used to determine the input.

2. **Base Case:** 
    - If `n` is less than 1000, return 0, as there are no commas used for numbers with less than four digits.

3. **Calculation:**
    - If `n` is greater than or equal to 1000, increment `count` by `n`. 
    - Increment the `count` variable by 1 to account for the comma.
    - Subtract 1000 from `n` to eliminate commas for numbers with 4 digits or more.
    - Return `count`.

## Complexity Analysis
* **Time Complexity:** $O(1)$
    * The algorithm's complexity is determined by the number of iterations.
* **Space Complexity:** $O(1)$
    * The algorithm uses a constant amount of space.