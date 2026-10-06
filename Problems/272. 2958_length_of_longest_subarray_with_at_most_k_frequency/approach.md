# Problem 2958: Length of Longest Subarray With at Most K Frequency

## Intuition
The core idea is to use a sliding window technique to efficiently determine the length of the longest good subarray. We iterate through the array, keeping a `freq_tracker` dictionary to track the frequency of each element.  We maintain a `left` pointer to define the start of the window, and a `max_length` variable to track the maximum length of a good subarray encountered.

## Approach
1. **Initialization:** 
   -  `n`: Stores the length of the input array `nums`.
   -  `freq_tracker`: A dictionary that stores the frequency of each element in the `nums` array. It is initialized as an empty dictionary. 
   -  `left`: Represents the start of the sliding window. It's initialized as 0. 
   -  `max_length`: Represents the maximum length of a good subarray, initialized as 0.

2. **Sliding Window:**
   -  `for right in range(n):`: We iterate through the input array `nums` using a `right` pointer. 
   -  `freq_tracker[nums[right]] = freq_tracker.get(nums[right], 0) + 1`:  For each element at index `right`, we update its frequency in the `freq_tracker` dictionary, incrementing it by 1.
   -  `while freq_tracker[nums[right]] > k:`:  If the current element's frequency exceeds `k`, we shrink the window from the left.
      -  `freq_tracker[nums[left]] -= 1`:  Decrement the frequency of the element at the left pointer (representing the previous element in the window).
      -  `left += 1`: Increment the `left` pointer to slide the window. 
   -  `current_max_length = right - left + 1`: Calculate the length of the current good subarray (from `left` to `right`).
   -  `max_length = max(current_max_length, max_length)`: Update `max_length` if the current subarray length is longer than the previous one.

3. **Return:**
   -  `return max_length`:  Return the maximum length of the good subarray found.


## Complexity Analysis
* **Time Complexity:** $O(n)$
    * We iterate through the array once, which has a time complexity of `O(n)`.
    * The `freq_tracker` dictionary is accessed `O(1)` time for each element, leading to a time complexity of `O(n)`.

* **Space Complexity:** $O(n)$
    * The `freq_tracker` dictionary has a size proportional to the number of elements in the array.