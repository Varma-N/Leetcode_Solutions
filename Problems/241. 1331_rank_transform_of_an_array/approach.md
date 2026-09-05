# Problem 1331: Rank Transform of an Array

## Intuition
The algorithm leverages the `rankdata` function from the `scipy.stats` module to efficiently compute the rank of each element in the input array. The `rankdata` function utilizes a pre-implemented sorting algorithm to quickly determine the rank of each element based on its value, effectively solving the problem by using the inherent ordering of the array.

## Approach
1. **Import:** Import the necessary library, `scipy.stats`, to access the `rankdata` function.

2. **Function Definition:** Define a class `Solution` with a method `arrayRankTransform` that takes an integer array `arr` as input and returns a list of integers representing the ranks of the elements.

3. **Rank Calculation:**
   *  Call the `rankdata` function from `scipy.stats`, specifying the `method` argument as `"dense"` to calculate the rank data with dense ordering (meaning the rank is directly derived from the positions of the elements).
   *  Convert the resulting rank data into a list using the `.tolist()` method.

4. **Output:** Return the list of ranks.

## Complexity Analysis
* **Time Complexity:** $O(N \log(N))$, where N is the length of the input array. 
    * The `rankdata` function operates in linear time, $O(N \log(N))$, due to the efficient sorting algorithm it employs. 

* **Space Complexity:** $O(1)$, as the algorithm only uses a constant amount of extra space for the `rankdata` function's input and output.