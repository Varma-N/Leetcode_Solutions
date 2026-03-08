# Approach: Sliding Window with Two Heaps

## Overview
The problem requires dividing an array into `k` subarrays such that the sum of the first elements of each subarray is minimized. The starting indices of adjacent subarrays must satisfy a distance constraint `dist`. Since the first subarray always starts at index `0`, `nums[0]` is a fixed cost. The goal is to efficiently select the remaining `k-1` starting indices with the smallest values within the valid sliding window ranges.

This solution employs a **Sliding Window** technique combined with **Two Heaps** to maintain the smallest `k-1` elements dynamically as the window moves across the array.

## Key Data Structures
1.  **Max-Heap (`lo`)**: Stores the smallest `k-1` elements currently in the window. Since standard libraries typically provide min-heaps, negative values are stored to simulate a max-heap. This allows efficient access to the largest element among the selected smallest values, which is necessary for swapping when a smaller candidate appears.
2.  **Min-Heap (`hi`)**: Stores the remaining elements in the window that are not among the smallest `k-1`.
3.  **Hash Maps (`lo_cnt`, `hi_cnt`)**: Implement **Lazy Deletion**. Because elements cannot be efficiently removed from the middle of a heap, these maps track the valid count of each number. When an element slides out of the window, its count is decremented. Elements are only physically popped from the heap top when they are encountered as invalid (count is zero).
4.  **Sum Tracker (`lo_sum`)**: Maintains the running sum of elements in the `lo` heap to avoid recalculating the cost at every step.

## Step-by-Step Algorithm

1.  **Initialization**:
    *   Determine `need = k - 1`, the number of additional subarray starts required.
    *   Populate the initial window (indices `1` to `1 + dist`) by adding all elements to the `hi` heap.
    *   **Rebalance**: Transfer the smallest `need` elements from `hi` to `lo` to ensure `lo` holds the optimal candidates.
    *   Ensure ordering invariant: The largest element in `lo` must be less than or equal to the smallest element in `hi`. Swap if necessary.
    *   Calculate the initial minimum cost using `nums[0] + lo_sum`.

2.  **Sliding the Window**:
    *   Iterate through the array, shifting the window one position to the right.
    *   **Remove Outgoing Element**: Identify the element leaving the left side of the window. Decrement its count in the corresponding hash map and update the heap size and `lo_sum` if it belonged to `lo`.
    *   **Add Incoming Element**: Identify the new element entering the right side of the window. Add it to `hi`, increment its count, and update the heap size.

3.  **Maintaining Invariants**:
    After each slide, rebalance the heaps to satisfy three conditions:
    *   **Capacity**: Ensure `lo` contains exactly `need` elements. If underfilled, move the smallest from `hi` to `lo`. If overfilled, move the largest from `lo` to `hi`.
    *   **Ordering**: Ensure `max(lo) <= min(hi)`. If `max(lo) > min(hi)`, swap these two elements between the heaps.
    *   **Lazy Cleanup**: Before accessing heap tops, remove any elements that have a zero count in their respective hash maps (indicating they are no longer in the window).

4.  **Update Minimum Cost**:
    *   After rebalancing, `lo_sum` represents the sum of the smallest valid `k-1` elements for the current window position.
    *   Update the global minimum answer: `ans = min(ans, nums[0] + lo_sum)`.

5.  **Return Result**:
    *   Once the window has slid through all valid positions, return the recorded minimum cost.

## Complexity Analysis

### Time Complexity: $O(N \log N)$
*   **Window Sliding**: The algorithm iterates through the array once, performing operations for each of the $N$ elements.
*   **Heap Operations**: Each element is pushed and popped from the heaps a constant number of times. Heap operations take $O(\log S)$, where $S$ is the heap size (up to $N$).
*   **Lazy Removal**: Stale elements are removed from the heap tops exactly once over the course of the execution.
*   The dominant factor is the heap operations performed $N$ times, resulting in $O(N \log N)$.

### Space Complexity: $O(N)$
*   **Heaps**: In the worst case, the heaps store all elements within the window, requiring $O(N)$ space.
*   **Hash Maps**: The dictionaries tracking element counts also require $O(N)$ space in the worst case.
*   Total auxiliary space is linear with respect to the input size.
