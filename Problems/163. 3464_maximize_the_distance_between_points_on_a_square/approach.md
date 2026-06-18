# Problem 3464: Maximize the Distance Between Points on a Square

## Intuition
A key insight is to consider the Manhattan distance between two points on the boundary of the square. By strategically selecting `k` points, we can maximize the distance between them by placing points on the boundary and considering their relative positions in the form of (xi, yi) where side is the side length of the square.  This approach leverages the inherent arrangement of points within a square to achieve a high minimum Manhattan distance.


## Approach
1. **Calculate Manhattan Distances:** Calculate the Manhattan distance for each pair of points on the boundary, considering their position in relation to one another. 

2. **Sort Points:** Organize the points based on their calculated distances in order from smallest to largest. This ensures we consider the most efficient pairings for maximizing the distance.

3. **Place `k` points strategically:** Select a subset of `k` points from the sorted array. The optimal arrangement is determined by the Manhattan distance between the selected points. 


## Complexity Analysis
* **Time Complexity:** $O(N \log N)$ (sorting) + $O(N)$ (calculation of distances).
    * We sort the points in O(N log N), and we calculate the Manhattan distance for each pair, which takes a constant time.  

* **Space Complexity:**  $O(1)$ 
    * The algorithm's space complexity is independent of the input size.