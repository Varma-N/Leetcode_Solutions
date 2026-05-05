# 3600. Maximize Spanning Tree Stability with Upgrades

## Problem Strategy

The goal is to find a set of edges that forms a Spanning Tree where the minimum strength of any edge (stability) is maximized. We have a budget of `k` upgrades to double the strength of optional edges.

### 1. Categorization and Edge Cases
*   **Divide Edges**: Separate the edges into **Mandatory** and **Optional** groups based on their "must" flag.
*   **Mandatory Constraints**: Any mandatory edge included sets an upper bound on the final stability, as the stability cannot exceed the minimum strength of these required edges.
*   **Cycle Detection**: If the mandatory edges already form a cycle, it is impossible to form a valid tree. Return -1.

### 2. Connectivity Pre-Check
*   Verify if the graph can be fully connected using every available edge (both mandatory and optional).
*   If the number of connected components remains greater than 1 after processing all edges, a spanning tree is impossible. Return -1.

### 3. Binary Search for Optimal Stability
*   Perform a binary search for the highest possible stability value `mid`.
*   The search range starts from 1 up to the minimum strength of the mandatory edges (or the maximum possible upgraded value).

### 4. Feasibility Testing (Greedy Logic)
For a specific target stability `mid`, optional edges are treated as follows:
1.  **Free Edges**: Edges with strength $s \ge mid$. These can be used immediately.
2.  **Upgradable Edges**: Edges where $s < mid$ but $2s \ge mid$. These can be used at the cost of 1 upgrade.
3.  **Discarded Edges**: Edges where $2s < mid$ are ignored as they cannot meet the stability requirement.

**The Verification Process:**
*   Initialize a Disjoint Set Union (DSU) with all mandatory edges.
*   First, greedily add all **Free Edges** to connect components at zero cost.
*   If the graph is still not connected, add **Upgradable Edges** and increment a counter until the graph is connected or you run out of edges.
*   If the graph becomes a single component and the upgrades used $\le k$, the stability `mid` is possible.

## Complexity Analysis

*   **Time Complexity**: $O(E \log E + \log(S) \cdot E \alpha(N))$
    *   $E \log E$ is for sorting the optional edges by strength to enable efficient processing.
    *   $\log(S)$ represents the binary search iterations over the possible stability range.
    *   $E \alpha(N)$ covers the DSU (Union-Find) operations performed within each search step.
*   **Space Complexity**: $O(N + E)$
    *   Required to store the edge list and the DSU parent/rank arrays for $N$ nodes.
