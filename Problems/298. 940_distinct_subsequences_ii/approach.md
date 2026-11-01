# Problem 940: Distinct Subsequences II

## Intuition
The key idea is to leverage dynamic programming and the "ending-with" array to count distinct subsequences efficiently.  We essentially build up the count for each character and then account for the count of each subsequence formed.

## Approach
1. **Initialization:**
    * `MOD = 10**9 + 7`:  For modulo operations, we set `MOD` to 10^9 + 7.
    * `ends_with = [0] * 26`:  We initialize a list `ends_with` of size 26, each element representing the count of all the subsequences ending at that index of the string. 


2. **Iterate through the string:**
    * `for char in s:`: For each character in the string `s`, we proceed as follows. 
        * `idx = ord(char) - ord('a')`: We determine the index of the character in the alphabet.
        * `old_val = ends_with[idx]`: We store the previous count of the ends with the character to calculate the new count. 
        * `ends_with[idx] = (total + 1) % MOD`: We update `ends_with[idx]` to account for a subsequence ending at that index.  
        * `total = (total + ends_with[idx] - old_val) % MOD`: We calculate the total count of subsequences.

3. **Return `total`:**  The final count is returned.  

## Complexity Analysis
* **Time Complexity:** $O(N)$  where N is the length of the string.
    * We iterate through the string once. 
* **Space Complexity:** $O(26)$  where 26 represents the number of characters in the alphabet.
    * We use a list of size 26 to store the counts of subsequences.