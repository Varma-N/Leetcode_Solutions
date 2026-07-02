# Problem 3629: Minimum Jumps to Reach End via Prime Teleportation

## Intuition
The core idea is to utilize prime teleportation as an efficient tool to reach the end index of the array. We leverage information from the `spf` (smallest prime factor) array that provides the smallest prime number dividing each element in the input array, which is then used to determine reachable indices. 

The algorithm utilizes a breadth-first search approach. It begins at the starting point and explores all possible jumps to reach the desired end index by utilizing adjacent steps or Prime Teleportation based on the condition that the target index `i` needs to be able to be reached.


## Approach
1. **Initialization:**
   *  `max_val`: Determine the maximum value in the input array `nums`. 
   * `spf` Array: Create a list `spf` of size (maximum value + 1) initialized with values equal to their indices. The `spf` array will store the smallest prime number dividing each element in `nums`.
2. **Prime Factorization:**
   *  For every element `i` from 2 to the square root of `max_val`, iterate through all possible divisors (`i`) that are less than or equal to the current maximum value `j` (the square root is used to prevent unnecessary calculations) and set the smallest prime factor (`spf[j] = j`). This step creates a mapping of how each element can be reached via teleportation.
3. **Teleportation:** 
   *  To determine if teleporting is possible, check for the following: 
      *  `is_prime(val)`: Use `is_prime` to efficiently detect if the element `i` is prime.
4. **Breadth-First Search:**
    * Initialize a queue (`queue`) and a set of visited indices (`visited_indices`). Add starting index (0) with distance 0 to the queue.
    *  Iterate through the queue using a breadth-first search approach:
        * If we reach the end index, return the distance `dist`.
        * Explore adjacent jumps. For each `neighbor` within bounds and not visited, add it to the set of visited indices (`visited_indices`), then enqueue `neighbor` with updated distance (`dist + 1`).
5. **Teleportation Optimization:** 
   *  If an element `p` is prime and not in the `visited_primes` set:
      * Add the index `i` to the `prime_to_indices` set. If a prime number `p` exists that can be teleported, then add every index `neighbor` where `p` is a factor (i.e., `p * neighbor`) to the `prime_to_indices`.
6. **Return:**  If no path to the target index is found, return -1.


## Complexity Analysis

* **Time Complexity:** $O(n)$ 
    * The algorithm explores all possible jumps using a breadth-first search approach which takes O(n) time. 

* **Space Complexity:** $O(n)$  
    * We use space proportional to the number of indices that need to be explored.