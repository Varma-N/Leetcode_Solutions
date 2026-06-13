# Problem 2078: Two Furthest Houses With Different Colors

## Approach

### Step-by-Step Breakdown

1.  **Analyze from the Right:**
    * Iterate backward from the last house (`n-1`) toward the first house (index `0`).
    * The first house we encounter that has a different color than the house at index `0` will provide the maximum possible distance starting from the beginning of the array. Store this distance as `rmax_dis`.
2.  **Analyze from the Left:**
    * Iterate forward from the first house (`0`) toward the last house (`n-1`).
    * The first house we encounter that has a different color than the house at index `n-1` will provide the maximum possible distance ending at the last house of the array. Store this distance as `lmax_dis`.
3.  **Compare and Return:**
    * The maximum distance between any two houses with different colors must involve either the first house or the last house as one of the endpoints.
    * Return the larger of the two calculated distances (`max(lmax_dis, rmax_dis)`).



## Complexity Analysis

* **Time Complexity:** $O(N)$
    * Where $N$ is the number of houses. In the worst case, we perform two linear scans of the array, both of which take $O(N)$ time.
* **Space Complexity:** $O(1)$
    * The algorithm uses a constant amount of extra space for integer variables (`n`, `right`, `left`, `rmax_dis`, `lmax_dis`), regardless of the input size.
