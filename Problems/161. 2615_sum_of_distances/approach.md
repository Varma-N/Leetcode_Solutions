```markdown
# Problem 2615: Sum of Distances

## Intuition
The core idea is to leverage the `prefix sum` technique. We will use it to calculate distances based on values in the input array (`nums`). Instead of directly calculating the distances, we utilize this technique by grouping indices with specific values and then applying the distance formula for each group. This approach simplifies calculations and leads to an efficient solution.

## Approach
1. **Grouping Indices:** First, we need to identify all indices that share a common value in `nums`.  We accomplish this using a `defaultdict` where keys are values from `nums`, and values are lists of corresponding indices (i.e., the array where values are present). 
2. **Summation for each group:** For each distinct value found, we calculate distances based on the `prefix sum` of the corresponding index values. The key here is to identify the sum of all the values in a group and then utilize this sum along with the prefix sum to determine the final distance.

## Complexity Analysis
* **Time Complexity:** $O(N)$ 
    *  We iterate through the array only once, grouping indices as needed. Then, within each group, we calculate the distances using a single loop and nested loops for the prefix sums.
* **Space Complexity:** $O(N)$ 
    * The code uses `defaultdict` for grouping by value, which utilizes constant space, independent of the input array size.