class Node:
    __slots__ = ['prod', 'pref']
    def __init__(self):
        self.prod = 1
        self.pref = [0] * 5
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        n = len(nums)
        tree = [None] * (4 * n)
        
        def merge(a: Node, b: Node) -> Node:
            res = Node()
            res.prod = (a.prod * b.prod) % k
            for i in range(k):
                res.pref[i] = a.pref[i]
            for i in range(k):
                res.pref[(a.prod * i) % k] += b.pref[i]
            return res

        def build(node: int, start: int, end: int):
            if start == end:
                tree[node] = Node()
                v = nums[start] % k
                tree[node].prod = v
                tree[node].pref[v] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node: int, start: int, end: int, idx: int, val: int):
            if start == end:
                v = val % k
                tree[node].prod = v
                for i in range(k):
                    tree[node].pref[i] = 0
                tree[node].pref[v] = 1
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def query(node: int, start: int, end: int, l: int, r: int) -> Node:
            if r < start or end < l:
                id_node = Node()
                id_node.prod = 1
                return id_node
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            left = query(2 * node, start, mid, l, r)
            right = query(2 * node + 1, mid + 1, end, l, r)
            return merge(left, right)

        build(1, 0, n - 1)
        ans = []
        
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            res = query(1, 0, n - 1, start, n - 1)
            ans.append(res.pref[x])
             
        return ans
