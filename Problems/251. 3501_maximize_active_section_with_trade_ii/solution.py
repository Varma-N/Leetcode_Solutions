from typing import List

class Node:
    __slots__ = ['max_Z', 'min_O', 'max_Z_plus_Z', 'first_Z', 'last_Z', 'has_Z']
    
    def __init__(self):
        self.max_Z = 0
        self.min_O = float('inf')
        self.max_Z_plus_Z = 0
        self.first_Z = 0
        self.last_Z = 0
        self.has_Z = False

def merge(left: Node, right: Node, O_mid: int) -> Node:
    if not left.has_Z:
        return right
    if not right.has_Z:
        return left

    res = Node()
    res.has_Z = True
    res.max_Z = max(left.max_Z, right.max_Z)
    res.min_O = min(left.min_O, right.min_O, O_mid)
    res.max_Z_plus_Z = max(left.max_Z_plus_Z, right.max_Z_plus_Z, left.last_Z + right.first_Z)
    res.first_Z = left.first_Z
    res.last_Z = right.last_Z
    return res

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        blocks = []
        block_id = [0] * n
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            for k in range(i, j):
                block_id[k] = len(blocks)
            blocks.append((int(s[i]), j - i))
            i = j

        num_blocks = len(blocks)
        tree = [Node() for _ in range(4 * num_blocks)]

        def build(node, start, end):
            if start == end:
                if blocks[start][0] == 0:
                    tree[node].has_Z = True
                    tree[node].max_Z = blocks[start][1]
                    tree[node].first_Z = blocks[start][1]
                    tree[node].last_Z = blocks[start][1]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            O_mid = float('inf')
            if blocks[mid][0] == 1:
                O_mid = blocks[mid][1]
            elif mid + 1 <= end and blocks[mid + 1][0] == 1:
                O_mid = blocks[mid + 1][1]
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], O_mid)

        if num_blocks > 0:
            build(1, 0, num_blocks - 1)

        def query_tree(node, start, end, l, r):
            if l > end or r < start:
                return Node()
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            left = query_tree(2 * node, start, mid, l, r)
            right = query_tree(2 * node + 1, mid + 1, end, l, r)
            O_mid = float('inf')
            if blocks[mid][0] == 1:
                O_mid = blocks[mid][1]
            elif mid + 1 <= end and blocks[mid + 1][0] == 1:
                O_mid = blocks[mid + 1][1]
            return merge(left, right, O_mid)

        total_ones = s.count('1')
        ans = []

        start_idx_of_block = [0] * num_blocks
        curr_idx = 0
        for idx in range(num_blocks):
            start_idx_of_block[idx] = curr_idx
            curr_idx += blocks[idx][1]

        for L, R in queries:
            bL = block_id[L]
            bR = block_id[R]

            if bL == bR:
                ans.append(total_ones)
                continue

            res = Node()
            if bL + 1 <= bR - 1:
                res = query_tree(1, 0, num_blocks - 1, bL + 1, bR - 1)

            left_node = Node()
            if s[L] == '0':
                left_node.has_Z = True
                length = blocks[bL][1] - (L - start_idx_of_block[bL])
                left_node.max_Z = length
                left_node.first_Z = length
                left_node.last_Z = length

            right_node = Node()
            if s[R] == '0':
                right_node.has_Z = True
                length = R - start_idx_of_block[bR] + 1
                right_node.max_Z = length
                right_node.first_Z = length
                right_node.last_Z = length

            O_left = float('inf')
            O_right = float('inf')

            if s[L] == '1' and left_node.has_Z:
                O_left = blocks[bL + 1][1]
            elif s[L] == '0' and bL + 1 <= bR and blocks[bL + 1][0] == 1:
                O_left = blocks[bL + 1][1]

            if s[R] == '1' and right_node.has_Z:
                O_right = blocks[bR - 1][1]
            elif s[R] == '0' and bR - 1 >= bL and blocks[bR - 1][0] == 1:
                O_right = blocks[bR - 1][1]

            final_res = Node()
            if left_node.has_Z:
                final_res = merge(left_node, res, O_left)
                if right_node.has_Z:
                    final_res = merge(final_res, right_node, blocks[bR - 1][1] if blocks[bR - 1][0] == 1 else float('inf'))
            else:
                final_res = res
                if right_node.has_Z:
                    final_res = merge(final_res, right_node, O_right)

            max_gain = 0
            if final_res.has_Z and final_res.min_O != float('inf'):
                max_gain = max(final_res.max_Z_plus_Z, final_res.max_Z - final_res.min_O)

            ans.append(total_ones + max_gain)

        return ans