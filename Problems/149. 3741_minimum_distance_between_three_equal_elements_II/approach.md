# Step-by-Step Approach

1. **Initialize Data Structures**: Create a map (dictionary) to store the occurrences of each element. The keys will be the elements from the array, and the values will be lists of indices where these elements are found.
2. **Populate the Map**: Iterate through the input array element by element. For each element, append its current index to the corresponding list in the map. Since the array is traversed from left to right, the indices in these lists will naturally be sorted in ascending order.
3. **Initialize Tracking Variables**: Set a minimum distance variable to infinity to keep track of the smallest computed distance. Set a boolean flag (e.g., `found`) to false to track if we encounter any element that appears at least three times.
4. **Evaluate Distances**: Iterate through the map, examining the list of indices for each unique element.
5. **Check Frequency**: If an element's index list contains 3 or more indices, set the `found` flag to true and proceed to calculate the distance. If it contains fewer than 3 indices, skip to the next element.
6. **Calculate Sliding Window Distance**: For an element with at least 3 occurrences, iterate through its index list using a sliding window of size 3 (i.e., looking at indices at position `i` and `i+2`). Compute the distance using the specific formula provided: `2 * (indices[i+2] - indices[i])`.
7. **Update Minimum Distance**: Compare the newly calculated distance with the current minimum distance tracking variable. If the newly calculated distance is strictly smaller, update the minimum distance.
8. **Return the Result**: After evaluating all groups of elements, return the minimum distance if the `found` flag is true. If no element appeared at least three times (meaning the flag remained false), return `-1`.

## Complexity Analysis

* **Time Complexity**: **O(N)**, where `N` is the number of elements in the input array. We iterate through the array once to populate the map, which takes `O(N)` time. Then, we iterate through the map to evaluate the indices. Because the sum of the lengths of all index lists in the map is exactly `N`, checking the windows takes `O(N)` overall operations. Thus, the total time complexity is linear.
* **Space Complexity**: **O(N)**, where `N` is the number of elements in the array. The space is primarily consumed by the map, which in the worst case (or any case) will store all `N` indices grouped by their values.
