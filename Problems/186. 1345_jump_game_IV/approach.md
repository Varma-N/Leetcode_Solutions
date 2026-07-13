# Problem 1345: Jump Game IV

## Intuition
The core idea is to use a breadth-first search (BFS) approach on the graph of reachable positions.  We start at the initial position and explore all possible jumps to reach the end index by using BFS. The algorithm leverages the adjacency list representation for representing the graph to efficiently track neighbors of each node.

## Approach
1. **Initialization:** 
    - `n`: Store the length of the input array `arr`.
    - `graph`: A dictionary where keys represent values from `arr` and values are lists of indices reachable by jumps from that value.
        - For every element in `arr`, add its value as a key, and append the corresponding index as values in the list.

2. **BFS Traversal:** 
    -  Create a queue `queue` to store starting positions (index 0). 
    - Initialize `visited` set to track visited indices during BFS traversal (initially only index 0 is included).
    - `steps`: Keep track of the number of jumps.
    - **While `queue` is not empty:** 
        - Iterate through elements in `queue`.
        - If the current position (`curr`) equals the last index, return the current `steps`.
        - For each neighbor of `curr`:
            - If neighbor is not visited:
                - Add neighbor to `visited`.
                - Enqueue `neighbor` to queue.

3. **Expanding Search Space:** 
    - After exploring all neighbors from a position, clear the list associated with that position in graph (`graph[arr[curr]]`).
    - Update `steps`: 
        - If the current index plus 1 is within bounds and not visited, add it to queue and mark as visited.
        - If the current index minus 1 is within bounds and not visited, add it to queue and mark as visited.

4. **Looping & Return:** 
    - Continue this process for every jump until the queue is empty. 
    - The algorithm terminates when a valid path from the starting position is found (i.e., reaching the end index), or when all reachable positions have been explored (`steps` reaches the maximum).

**Complexity Analysis**

* **Time Complexity:**  O(N * m) , where N is the array length and m is the number of nodes in the graph (the size of the adjacency list, calculated from the input array). The algorithm iterates through the array to build the graph.
    * Each element's value represents a node in the graph.
    * For each node, we explore all its possible jumps in BFS.

* **Space Complexity:** O(N) for the queue, visited set, and graph dictionary, where N is the size of the input array.
