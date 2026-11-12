# Problem 1520: Maximum Number of Non-Overlapping Substrings

## Intuition
The problem asks for the maximum number of non-overlapping substrings of a given string `s` that satisfy specific conditions. The key insight is to use a technique based on "sliding window" and "prefix-sums" to efficiently identify and store these non-overlapping substrings. 

## Approach

1. **Build Prefix-Sums:** Create a `first` dictionary to store the last index of each character in the string `s`, using `s.find(c)`.  Similarly, create a `last` dictionary to store the first index of each character in the string `s`, using `s.rfind(c)`.

2. **Identify Non-Overlapping Substrings:** Iterate through the alphabet (or a set of characters) and for each character:
   -  Calculate the start and end of a potential substring by using the `first` and `last` dictionary.
   -  If the substring doesn't overlap, add the substring to `intervals`. 
3. **Sort Intervals:** Sort the `intervals` in ascending order of their end points. 
4. **Construct Substrings:** Loop through the sorted intervals and use the `last_end` variable to ensure that only non-overlapping substrings are added to the `res` list.


## Complexity Analysis

* **Time Complexity:** $O(N)$, where N is the length of the string. The dominant factor in the time complexity is the creation of the `first` and `last` dictionaries.  

* **Space Complexity:** $O(1)$. The space complexity is constant, as we only store a fixed number of integers to store the information about the substrings.