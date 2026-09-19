```markdown
# Problem 628: Maximum Product of Three Numbers

## Intuition
To find the maximum product of three numbers in an array, we can utilize a greedy approach.  We first need to identify the three smallest numbers in the array, and then the three largest.  We use these smallest and largest numbers to find the maximum product.

## Approach
The following steps outline how to find the maximum product of three numbers in an array:
1. **Initialization**: We initialize three variables:
   * `min1` to infinity
   * `min2` to infinity
   * `max1` to negative infinity
   * `max2` to negative infinity
   * `max3` to negative infinity
2. **Iteration**: We iterate through the input array `nums`.
3. **Update**: 
   * If the current element `n` is less than or equal to `min1`, we update `min2` to `min1`, and `min1` to `n`.
   * If `n` is less than or equal to `min2`, we update `min2` to `n`.
   * If `n` is greater than or equal to `max1`, we update `max3` to `max2`, `max2` to `max1`, and `max1` to `n`.
   * We do the same for `max2` if it is less than or equal to `max1`.
4. **Finding Maximum Product**: We return the maximum of `min1 * min2 * max1` and `max1 * max2 * max3`.

## Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through the input array once, with the time complexity of O(N).
* **Space Complexity:** $O(1)$
    * The algorithm only uses a few variables to store the minimum and maximum values, which is constant in terms of space complexity.