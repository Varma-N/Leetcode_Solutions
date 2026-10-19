# Problem 3718: Smallest Missing Multiple of K

## Intuition
The smallest missing multiple of k can be found by iterating through the input array `nums`, and building a `set` of the multiples of k. We then use the `while` loop to find the smallest multiple of k that is not in the `set`.

## Approach
1. **Initialization:**
   - `multiple_set = set(nums)`: We create a set `multiple_set` containing all the elements in the `nums` array. 
   - `multiple = k`:  We initialize `multiple` to `k` which is the target multiple.
2. **Finding the Missing Multiple:**
   - `while k in multiple_set:`:  We use a `while` loop to iterate through the `multiple_set` while `k` is present in it.
     - `k += multiple`: Inside the loop, `k` is incremented by the `multiple`. 
   - `return k`: Once `k` is no longer in the `set`, the loop terminates, and `k` is returned as the smallest missing multiple.
 
## Complexity Analysis
* **Time Complexity:** $O(N)$
    * We iterate through `nums` once and build the `set` in constant time.
* **Space Complexity:** $O(N)$
    * The `set` of `nums` can store a maximum of `N` elements.