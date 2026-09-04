# Problem 2685: Count the Number of Complete Components

## Intuition
A complete component is a subgraph in which every pair of vertices is connected, and every edge is used. This can be achieved by performing Depth First Search (DFS) and counting the number of edges that are used to connect all the vertices.


## Approach
1. **Graph Representation:** Create an adjacency list `adj` for the graph. Each index in `adj` represents a vertex and stores a list of its adjacent vertices. 
    * Iterate through each edge in `edges` and add the corresponding edges to `adj`. 
    * The added edges represent the connection between the vertices.
2. **Initialization:** Initialize `visited` set to store the visited vertices during DFS and `ans` to store the count of complete components. 
3. **DFS Exploration:** Iterate through each vertex in `range(n)`.
    * If the vertex `i` is not visited, start a DFS from vertex `i` using `q` (a deque) to store the vertices to be visited. 
    * Inside the loop:
        * Increment `comp_nodes` as we explore a new node.
        * Increment `comp_edges` as we find edges that connect the nodes and update the count of connections.
        * Append unvisited neighbors to `q` to continue exploring the graph.
    * After exploring all reachable nodes, if `comp_edges // 2` is equal to the number of `comp_nodes` multiplied by `(comp_nodes - 1) // 2` then it is a complete component. We increment `ans` and continue.
4. **Return:** Return the `ans` variable, which stores the count of complete components.

## Complexity Analysis
* **Time Complexity:** $O(N + E)$ where $N$ is the number of vertices and $E$ is the number of edges. We explore each vertex exactly once and DFS explores edges and vertices in the graph. 
    * The number of edges can be $O(N \cdot (N-1))$
* **Space Complexity:** $O(N)$ due to the adjacency list.