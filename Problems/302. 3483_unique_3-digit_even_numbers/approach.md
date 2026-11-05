# Problem 3483: Unique 3-Digit Even Numbers

## Intuition
The solution exploits the fact that an even number can be formed by having a combination of digits from the provided array, where the sum of the digits is divisible by 2. The process of finding the unique combinations of digits for a three-digit number, then checking if it is even is the core of the solution.  

## Approach
1. **Generate all permutations:** Use `itertools.permutations(digits, 3)` to create all possible 3-digit numbers using the given digits. 
2. **Check for divisibility by 2:** For each permutation, check if the number is even by using the bitwise AND operator.  
3. **Remove duplicates:** Use a `set` to store the unique even numbers.  


## Complexity Analysis
* **Time Complexity:** $O(N!)$, where N is the number of digits.
    * We generate all permutations, and the time complexity is dominated by the factorial of the number of digits. 
* **Space Complexity:** $O(N)$ 
    * The use of a set to store unique numbers has a space complexity of O(N)