# 1415. The k-th Lexicographical String of All Happy Strings of Length n

### Approach Step-by-Step

1.  **Calculate Total Possibilities**: 
    Determine the total number of "happy strings" of length $n$. Since the first character has 3 choices ('a', 'b', or 'c') and each subsequent character has 2 choices (any of the three except the previous one), the total count is $3 \times 2^{n-1}$.

2.  **Check Feasibility**: 
    If the requested index $k$ is greater than the total number of possible happy strings, return an empty string immediately as the solution is unreachable.

3.  **Iterative Character Selection**: 
    Build the string character by character from left to right (from index $0$ to $n-1$). For each position, the remaining combinations can be divided into equal-sized "buckets."

4.  **Determine Bucket Size**: 
    For a position $i$, the number of possible strings that can be formed with the remaining $(n - 1 - i)$ characters is $2^{n - 1 - i}$. This represents the size of the range covered by choosing one valid character at the current position.

5.  **Lexicographical Character Choice**: 
    Iterate through the available characters ('a', 'b', 'c') in alphabetical order. 
    * **Skip Invalid Characters**: If the current character is the same as the last character added to the result, skip it to maintain the "happy string" property.
    * **Compare $k$ to Bucket Size**: 
        * If $k$ is less than or equal to the current bucket size, the $k$-th string must start with this character. Append it to the result and move to the next position.
        * If $k$ is greater than the bucket size, it means the $k$-th string lies beyond the range of the current character. Subtract the bucket size from $k$ and try the next available character.

6.  **Final Construction**: 
    Once all $n$ characters are selected, join them to form the final happy string.

### Complexity Analysis

* **Time Complexity**: $O(n)$, where $n$ is the length of the string. The algorithm iterates $n$ times, and for each position, it checks at most 3 characters.
* **Space Complexity**: $O(n)$ to store the characters of the resulting string before joining them.
