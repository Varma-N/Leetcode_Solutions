# Problem 1967: Number of Strings That Appear as Substrings in Word

## Intuition
The provided solution uses a straightforward approach to efficiently determine the number of patterns that are substrings of the given word. The core idea is to iterate through each pattern in the `patterns` list and check if it exists as a substring of the `word`. We increment a counter for each instance of a pattern appearing as a substring. 

## Approach
1. **Initialization:**  
    - `count = 0`: Initialize a counter to keep track of the number of patterns found as substrings.

2. **Iterating through Patterns:** 
    - `for pattern in patterns:`: Loop through each pattern in the `patterns` list.

3. **Substring Check:** 
    - `if pattern in word:`: Inside the loop, check if the current `pattern` exists as a substring within the `word`.
    - `count += 1:` If the `pattern` is a substring of `word`, increment the `count`.

4. **Returning the Count:** 
    - `return count:` After checking all patterns, return the final `count`, representing the number of patterns that are substrings of `word`.

## Complexity Analysis
* **Time Complexity:** $O(patterns.length \times word.length)$ 
    * The dominant factor is the loop iterating through all patterns and the `in` operator checks. The number of pattern-string comparisons is proportional to the length of the patterns and the word.
* **Space Complexity:** $O(1)$ 
    * The space complexity is constant because only a few variables are used, such as `count` and the `patterns` list.
