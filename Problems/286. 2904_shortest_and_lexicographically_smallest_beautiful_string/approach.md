# Problem 2904: Shortest and Lexicographically Smallest Beautiful String

## Intuition
A beautiful string is one where the number of '1's is exactly 'k'. The lexicographically smallest beautiful string is the lexicographically smallest substring of length 'len' that satisfies this condition. We can achieve this by iterating through the string and building beautiful substrings by checking if the count of '1's is 'k'. We can also find the lexicographically smallest beautiful substring.

## Approach
1. **Initialize:**
   - `left`: pointer to the start of the substring (0)
   - `right`: pointer to the end of the substring (0)
   - `ones_count`: count of '1's in the current substring (0)
   - `best`: store the lexicographically smallest beautiful substring (None) 
2. **Iterate:**
   - While `right` is within the string length:
     - If `s[right]` is '1', increment `ones_count`.
     - **Inner Loop:**
       - While `ones_count == k` :
         -  Extract the current substring: `current_sub = s[left:right+1]`
         -  If `best` is None or  the substring is lexicographically smaller than `best`:
           - Update `best`
         -  Decrement `ones_count`
         -  Increment `left`
     - Increment `right`
3. **Return:**
   - Return `best` if it's not `None`, otherwise, return ""

## Complexity Analysis
* **Time Complexity:** $O(N)$  
    * We iterate through the string once, where N is the length of the string.
* **Space Complexity:** $O(1)$  
    * We use a constant amount of extra space for variables (time complexity)