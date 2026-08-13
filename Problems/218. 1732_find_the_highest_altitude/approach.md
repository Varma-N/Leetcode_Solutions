# Problem 1732: Find the Highest Altitude

## Intuition
The key is to maintain a running sum of altitudes while traversing through the gain array. This sum will track the highest altitude encountered during the trip. 

## Approach
1. **Initialization:** Initialize `res` with negative infinity to ensure any positive value found in the loop will be higher.
2. **Iterative Calculation:** Iterate through the `gain` array using a for loop (index `i`). 
   *  **Update `current` Altitude:** Add the current gain value (`i`) to the running `current` altitude. This represents the net change in altitude between consecutive points.
   *  **Check & Update `res`:** Compare the `current` altitude with the current `res`. If the `current` altitude is higher, update `res` to store this new maximum. 
3. **Return Result:** Return the maximum value of `res`, taking care of a potential minimum of 0 by applying `max(0, res)`.

**Key Observations and Logic:** This approach exploits the cumulative nature of altitudes over the trip. The sum is directly proportional to the highest altitude achieved at any point on the trip.


## Complexity Analysis
* **Time Complexity:** $O(N)$ where N is the length of the `gain` array. 
    * The loop iterates through the entire array once, requiring only O(N) time.
* **Space Complexity:** $O(1)$ 
    *  We are maintaining a single variable, `res`, for storing the highest altitude encountered during the trip.