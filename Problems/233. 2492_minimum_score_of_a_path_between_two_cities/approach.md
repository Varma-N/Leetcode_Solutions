# Problem 2492: Minimum Score of a Path Between Two Cities

## Intuition
A path between two cities in a graph is a sequence of roads connecting them, where the minimum score of a path is the shortest distance on the path, given by the minimum distance of a road between two cities in the path. The approach involves using a Breadth First Search (BFS) algorithm to traverse the graph and find the shortest path.

## Approach
1. **Initialization:**
   - `graph`: A defaultdict is used to represent the graph where keys represent cities and values are lists of neighbors and corresponding edge weights. 
   - `min_score`: Initialized to infinity, representing the initial minimum path score.
   - `visited`: A set to track visited nodes during the BFS traversal. 
   - `queue`: A deque used for BFS, initialized with city 1.
2. **BFS traversal:**
   - While the queue is not empty:
     - Dequeue a node from the front of the queue (`node`).
     - Iterate through the neighbors of the current node:
        - If the neighbor is not in the visited set:
           - Add the neighbor to the visited set.
           - Enqueue the neighbor to the queue for further exploration. 
     - Update `min_score` by comparing the current path score (`weight`) with the existing `min_score`. 
3. **Result:** Return `min_score` as the minimum score of a path between cities 1 and n.

## Complexity Analysis
* **Time Complexity:**  $O(V + E)$, where V is the number of cities and E is the number of edges. The BFS traversal visits each city and edge at most once. 
* **Space Complexity:** $O(V)$ for the visited set, which stores the vertices visited during the BFS.