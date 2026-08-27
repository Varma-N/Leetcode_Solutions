# Problem 3620: Network Recovery Pathways

## Intuition
A valid path from node 0 to node n-1 in a directed acyclic graph with recovery costs is determined by finding paths that meet certain conditions: all nodes must be online, and the total cost must not exceed a given limit. The goal is to find the maximum minimum-edge cost along all valid paths. This problem can be solved using a Depth First Search (DFS) approach to identify all valid paths and then the minimum cost for each path.

## Approach
1. **Initialization:** 
    * Create an adjacency list `adj` to represent the graph. 
    * Initialize an `in_degree` array to store the incoming degree of each node. 
    
2. **Create Adjacency List:**
    * Iterate through the `edges` list:
        * If a node pair is online and connected (both nodes are online and have an edge between them), append the edge to the adjacency list, and increment the in-degree of the node the other node points to.
    
3. **Topological Sort:**
    * Use a topological sort algorithm (e.g., Kahn's algorithm) to determine the ordering of nodes such that all nodes with in-degree 0 will be part of the first layer of the topological sort.
    * Add nodes to the `top_order` list as they are processed, as they represent nodes with no pending dependencies.
 
4. **DFS Exploration:**
    * Initialize `low` and `high` as the lower and upper bounds for the exploration range of `mid`.
    * Set `ans` to -1 for initial state.
    * Use a binary search to find the optimal `mid` value for the `distance`. 
    
5. **Evaluate Valid Path:**
    * For each node `u` in the `top_order` list, explore paths using DFS. 
    * Calculate the `dist` array. 
    * If the `dist[n-1]` is less than or equal to `k`, update `ans` and adjust the lower bound (`low`).
    
    * Otherwise, adjust the upper bound (`high`).  

6. **Return `ans`:**
    * Finally, return the calculated `ans`.

 
## Complexity Analysis
* **Time Complexity:** $O(V + E)$
    *  The `topological_sort` takes $O(V + E)$ time, where $V$ is the number of nodes and $E$ is the number of edges. The `for loop` used for DFS takes $O(V + E)$ time.
* **Space Complexity:** $O(V)$
    *  The space complexity is dominated by the `adj` list, which stores the graph's adjacency information, with a size of $O(V)$.