# Problem 1288: Remove Covered Intervals

## Intuition
Removing covered intervals can be visualized as finding the "boundaries" of intervals. If an interval is completely contained within another, it's "covered." By sorting the intervals in ascending order of their starting points and then comparing the end points, we can efficiently determine which intervals are actually "covered."

## Approach
1. **Sort Intervals:** Sort the intervals in ascending order based on their starting points (first element).
2. **Initialization:**
    - `removed`: Initialize a counter to keep track of the number of intervals removed (starts at 0).
    - `max_end`: Initialize a variable to store the maximum ending point (starts at -1). 
3. **Iterate:** Loop through the sorted intervals.
    - **Covered Interval:** If the current interval's ending point (`end`) is less than or equal to the previously saved `max_end`, the current interval is covered by previous intervals.
    - **Removal:** Increment `removed` by 1 if the current interval is covered.
    - **Update `max_end`:** If the current interval's ending point is greater than the previously saved `max_end`, update `max_end` to this new ending point.
4. **Count Remaining Intervals:** After iterating through all intervals, the number of remaining intervals is determined by the difference between the original length of `intervals` and the number of intervals removed (`len(intervals) - removed`).
5. **Return:** Return the count of remaining intervals.
 

## Complexity Analysis
* **Time Complexity:** $O(N log N)$
    * Sorting the intervals in ascending order using `sort` function has a time complexity of $O(N log N)$.  
* **Space Complexity:** $O(1)$
    * We are using a constant amount of extra space for the `removed` counter and the `max_end` variable.