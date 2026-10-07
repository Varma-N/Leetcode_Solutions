# Problem 2213: Longest Substring of One Repeating Character

## Intuition
The solution utilizes a technique called "prefix sums" to efficiently identify the longest substring of one repeating character in a string after performing a series of queries.  We build a prefix sum array `sz` to represent the count of each character in the string.  We then use this array to efficiently determine the length of the longest substring of one repeating character.

## Approach
1. **Preprocessing**:
    * **Dynamic Programming**: Create a prefix sum array `sz` to store the counts of each character. 
    * **Initialization**: For every index `i` in the string `s` (0-indexed), store the length of the longest substring of one repeating character in the array `sz` at index `N + i`
    * **Updating the Prefix Sum Array**: Iterate through the string `s` and update the prefix sum array `sz` by adding 1 for each character. 

2. **Query Processing**:
    * **Looping**: Iterate through the `queryIndices` and `queryCharacters`
    * **Updating the Array**: For every query, use the prefix sum array `sz` and the `queryCharacters` to update the array `sz`

## Complexity Analysis
* **Time Complexity:** $O(N)$  
    *  The code iterates through the string only a maximum of 2*N times. 
* **Space Complexity:** $O(N)$ 
    * The `sz` array is used to store the counts of each character.
