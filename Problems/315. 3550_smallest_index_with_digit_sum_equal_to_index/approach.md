# Problem 3550: Smallest Index With Digit Sum Equal to Index

## Intuition
The goal of this problem is to find the smallest index in the given array `nums` where the sum of the digits at that index equals the index itself.  We can achieve this by iterating through the array and examining each element.  At each index, we calculate the sum of its digits. If this sum equals the index itself, we've found the desired index.

## Approach
1. **Initialization**: We start by initializing a loop to iterate through the input array `nums` using `enumerate` to access both the index (`i`) and value (`v`) of each element. 
2. **Digit Sum Calculation**: For each element `v` in the array, we initialize a variable `digit_sum` to zero and a temporary variable `temp` to copy the value of `v`. 
3. **Iterative Digit Sum Calculation**:  We then iterate through the digits of the current element `v` using a `while` loop.  
    * We use the modulo operator `%` to extract the rightmost digit and add it to `digit_sum`.
    * We use integer division `//` to remove the last digit. 
4. **Checking for Matching Index**:  After the loop, we check if `digit_sum` matches the current index `i`. If they match, we've found the target index, and we return `i`.  
5. **No Matching Index**: If the loop completes without finding a match, we return -1.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the array once. The time complexity is dominated by the loop iterating through the digits of each element.
* **Space Complexity:** $O(1)$
    * We only use a constant amount of extra space to store variables such as `digit_sum` and `temp`.