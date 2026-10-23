# Problem 2948: Make Lexicographically Smallest Array by Swapping Elements

## Intuition
The core idea is to leverage the lexicographical ordering of the array to efficiently rearrange elements. The idea is to find the closest pair of elements in the array and swap them. By doing this we can sort the array based on lexicographical order and thus minimize the number of swaps.


## Approach
1. **Sort the Array:** 
   - Sort the array `nums` based on the value of the elements in ascending order using `sorted()` function. The key to this method is that we are sorting based on the values of the elements. 
   
2. **Initialize `res` array:**
   - Create an `res` array of the same size as the input array. This array will hold the final lexicographically smallest array.

3. **Iterative Swapping:** 
   - We will use a `while` loop to iterate through the sorted array.
   - **Find Closest Pair:**
     - For each element in the sorted array, we will find the closest element (based on their difference) in the remaining array. 
   - **Swap Elements:**
      - Once we find the closest element, we swap the elements.  

## Complexity Analysis
* **Time Complexity:** $O(N \log N)$  
    * Sorting the array takes $O(N \log N)$ time using the `sorted()` function.
    * The remaining operations are linear time.

* **Space Complexity:** $O(N)$ 
    * The space complexity is linear because we are storing the final array in the `res` array.