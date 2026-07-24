class Node:
    __slots__ = ['has_obs', 'first_obs', 'last_obs', 'max_gap']
    def __init__(self, has_obs: bool, first_obs: int, last_obs: int, max_gap: int):
        self.has_obs = has_obs
        self.first_obs = first_obs
        self.last_obs = last_obs
        self.max_gap = max_gap

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        M = 0
        for q in queries:
            M = max(M, q[1])
        M = min(50005, M + 1)
        
        tree = [None] * (4 * M + 4)
        
        def merge(left: Node, right: Node) -> Node:
            has_obs = left.has_obs | right.has_obs
            if not left.has_obs and not right.has_obs:
                return Node(False, -1, -1, 0)
            elif left.has_obs and not right.has_obs:
                return Node(True, left.first_obs, left.last_obs, left.max_gap)
            elif not left.has_obs and right.has_obs:
                return Node(True, right.first_obs, right.last_obs, right.max_gap)
            else:
                return Node(
                    True,
                    left.first_obs,
                    right.last_obs,
                    max(left.max_gap, right.max_gap, right.first_obs - left.last_obs)
                )

        def build(node: int, start: int, end: int):
            tree[node] = Node(False, -1, -1, 0)
            if start == end:
                return
            mid = start + (end - start) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)

        def update(node: int, start: int, end: int, pos: int):
            if start == end:
                tree[node] = Node(True, pos, pos, 0)
                return
            mid = start + (end - start) // 2
            if pos <= mid:
                update(2 * node, start, mid, pos)
            else:
                update(2 * node + 1, mid + 1, end, pos)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def query(node: int, start: int, end: int, l: int, r: int) -> Node:
            if l <= start and end <= r:
                return tree[node]
            mid = start + (end - start) // 2
            if r <= mid:
                return query(2 * node, start, mid, l, r)
            if l > mid:
                return query(2 * node + 1, mid + 1, end, l, r)
            return merge(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r))

        build(1, 0, M)
        
        results = []
        for q in queries:
            if q[0] == 1:
                update(1, 0, M, q[1])
            else:
                x = q[1]
                sz = q[2]
                res = query(1, 0, M, 0, x)
                max_block = 0
                if not res.has_obs:
                    max_block = x
                else:
                    max_block = max(res.max_gap, res.first_obs, x - res.last_obs)
                results.append(max_block >= sz)
                
        return results   

        