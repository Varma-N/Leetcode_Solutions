# Problem 1848: Minimum Distance to the Target Element

## Step-by-Step Breakdown

1.  **Initialize Minimum Distance:** Start by setting a variable to hold the minimum distance. Initialize it to infinity so that the first valid distance found will easily overwrite it.
2.  **Iterate Through the Array:** Use a loop to scan through each element in the array, keeping track of the current index as you go.
3.  **Check for Target Match:** Inside the loop, check if the value at the current index matches the given `target` value.
4.  **Update Minimum Distance:** If the current element is the target, calculate the distance between its index and the given `start` index by taking the absolute difference. Update your minimum distance variable to hold the smaller value between its current state and this newly calculated distance.
5.  **Return Result:** After the loop finishes checking every element in the array, return the final stored minimum distance.

## Complexity Analysis

* **Time Complexity:** $O(N)$
    * $N$ is the number of elements in the array. The solution uses a single loop that iterates over every element exactly once. The operations inside the loop (equality check, absolute difference calculation, and minimum comparison) all take constant time $O(1)$. Therefore, the overall time complexity scales linearly with the size of the input array.
* **Space Complexity:** $O(1)$
    * The algorithm operates strictly in place using only a constant amount of extra memory. It only requires a few integer variables (for tracking the minimum distance and the loop index), which do not scale with the size of the input array.
