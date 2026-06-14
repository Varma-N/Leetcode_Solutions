from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        # Standard Union-Find Find function with path compression
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        # Union indices based on allowed swaps
        for u, v in allowedSwaps:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_u] = root_v

        # Group indices by their root parent
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        total_matches = 0
        
        # For each connected component, count common elements
        for root in groups:
            indices = groups[root]
            
            # Count frequencies of source elements in this component
            source_counts = defaultdict(int)
            for idx in indices:
                source_counts[source[idx]] += 1
            
            # See how many target elements can be satisfied
            for idx in indices:
                val = target[idx]
                if source_counts[val] > 0:
                    total_matches += 1
                    source_counts[val] -= 1
        
        return n - total_matches
