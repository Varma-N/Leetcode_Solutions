from typing import List
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        B = 150

        zeros = []
        large = []
        small = defaultdict(list)

        for l, r, k, v in queries:
            if l >= n: continue
            v %= MOD
            if v == 1: continue
            if v == 0:
                zeros.append((l, r, k))
                continue
            if k >= B:
                large.append((l, r, k, v))
            else:
                rem = l % k
                start = (l - rem) // k
                end = (r - rem) // k
                small[(k, rem)].append((start, end, v))

        for l, r, k in zeros:
            for i in range(l, r + 1, k):
                nums[i] = 0

        inv_cache = {}
        for (k, rem), qs in small.items():
            m = (n - 1 - rem) // k + 1
            diff = [1] * (m + 1)
            
            for start, end, v in qs:
                if end >= m: end = m - 1
                if start > end: continue
                
                diff[start] = (diff[start] * v) % MOD
                if end + 1 < m:
                    inv_v = inv_cache.get(v)
                    if inv_v is None:
                        inv_v = pow(v, MOD - 2, MOD)
                        inv_cache[v] = inv_v
                    diff[end + 1] = (diff[end + 1] * inv_v) % MOD

            curr = 1
            idx = rem
            for i in range(m):
                curr = (curr * diff[i]) % MOD
                if curr != 1:
                    nums[idx] = (nums[idx] * curr) % MOD
                idx += k

        for l, r, k, v in large:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD

        res = 0
        for x in nums:
            res ^= x
        return res
