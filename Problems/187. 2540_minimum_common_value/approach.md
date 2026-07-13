# Problem 2540: Minimum Common Value

## Intuition
The minimum common value of two sorted arrays can be efficiently determined by using a `set` data structure to quickly check for the presence of elements from both arrays. We iterate through the second array (`nums2`) and if an element is found within the first set, we return that value as the result. 

## Approach
1. **Input:** Two sorted integer arrays (`nums1` and `nums2`).
2. **Initialization**: Create a `set` called `nums1_set` using `set(nums1)`. This will allow us to efficiently check for the presence of an element in `nums1_set` within O(1) time complexity. 
3. **Iteration**: Loop through each element (`i`) in the array `nums2`.  
4. **Membership Check:** If the element `i` exists in `nums1_set`, it means that `i` is present in both sorted arrays, so return the value of `i` as the minimum common integer.  
5. **No Common Element:** If no elements are found from `nums2` in `nums1_set`, then we need to return -1. 


## Complexity Analysis
* **Time Complexity:** $O(N + M)$ where N is the length of `nums1` and M is the length of `nums2`. The loop iterates through `nums2` with a complexity of O(M), and checking if an element exists in the set takes O(1) time.  
* **Space Complexity:** $O(N)$ to store the elements in the set.