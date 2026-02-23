# Approach: Minimum Pair Removal to Sort Array I

## Step-by-Step Logic

1.  **Initial Verification**
    Start by checking if the input array is already sorted in non-decreasing order. If it is, no operations are needed, and the result is zero.

2.  **Iterative Simulation**
    If the array is not sorted, enter a loop that continues until the sorted condition is satisfied. This loop simulates the process of modifying the array step-by-step.

3.  **Identify Target Pair**
    Within each iteration, traverse the array to examine every adjacent pair of elements. Calculate the sum for each pair and identify the specific pair that produces the minimum sum. Keep track of both this minimum sum value and the starting index of the pair.

4.  **Perform Merge Operation**
    Once the target pair is identified, replace the two elements with a single element equal to their sum. This action reduces the total length of the array by one. Conceptually, this represents removing the pair and inserting their combined value back into the sequence.

5.  **Track Operations**
    Increment a counter variable by one to record that a removal and merge operation has been successfully performed.

6.  **Re-evaluate Condition**
    After modifying the array, check the sorted condition again. If the array remains unsorted, repeat the process from step 3 using the newly modified array.

7.  **Final Output**
    Once the loop terminates (meaning the array is fully sorted), return the total count of operations recorded.

## Complexity Analysis

### Time Complexity
**O(N²)**
In the worst-case scenario, the algorithm may need to perform a merge operation for nearly every element in the array, resulting in approximately N iterations of the outer loop. Inside each iteration, the algorithm performs multiple linear scans: one to verify if the array is sorted and another to find the adjacent pair with the minimum sum. Furthermore, the array reconstruction step (slicing and concatenation) involves copying elements, which is also a linear operation relative to the current array size. The combination of these nested linear operations results in quadratic time complexity.

### Space Complexity
**O(N)**
The algorithm requires additional memory to store the modified array during each iteration. Since the implementation creates new list objects during the slicing and concatenation process, the space required is proportional to the number of elements in the input array. No additional data structures scaling beyond the input size are used.
