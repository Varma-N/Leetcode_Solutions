# Problem 3536: Maximum Product of Two Digits

## Intuition
The key idea is to leverage the inherent structure of the input integer to identify the maximum product of two digits. We can achieve this by efficiently iterating through the digits of the integer and maintaining two variables, `highest` and `second_highest`, to track the largest and second-largest digits encountered so far. 

## Approach
1. **Initialization:**
    - Initialize two variables `highest` and `second_highest` to -1. These variables will track the largest and second-largest digits encountered during the iteration. 

2. **Iterating Through Digits:**
    - Convert the integer `n` to a string using `str(n)`.
    - Iterate through each character in the string representing the digits. 
    - For each digit `char`:
        - Convert `char` to an integer `digit`.
        - **Comparison & Update:**  
            - If `digit` is greater than `highest`:
                - Update `second_highest` to the previous `highest`. 
                - Set `highest` to the current `digit`.
            - If `digit` is greater than `second_highest` but less than or equal to `highest`:
                - Update `second_highest` to the current `digit`.

3. **Returning Maximum Product:**
    - After iterating through all the digits, return the product of `highest` and `second_highest`.


## Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the digits of the input integer `n` once, resulting in a time complexity of $O(N)$
* **Space Complexity:** $O(1)$
    * We only use a constant amount of extra space to store variables during the iteration, resulting in a space complexity of $O(1)$.