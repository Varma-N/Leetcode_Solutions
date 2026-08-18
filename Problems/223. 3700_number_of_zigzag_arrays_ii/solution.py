class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        def matmul(A, B):
            BT = list(zip(*B))
            return [[sum(a * b for a, b in zip(rowA, colB)) % MOD for colB in BT] for rowA in A]
        
        M = [[0] * k for _ in range(k)]
        for v in range(k):
            for u in range(k - v, k):
                M[v][u] = 1
                
        res = [[0] * k for _ in range(k)]
        for i in range(k):
            res[i][i] = 1
            
        p = n - 2
        base = M
        while p > 0:
            if p % 2 == 1:
                res = matmul(res, base)
            base = matmul(base, base)
            p //= 2
            
        A2 = list(range(k))
        total = 0
        for i in range(k):
            val = sum(res[i][j] * A2[j] for j in range(k)) % MOD
            total = (total + val) % MOD
            
        return (total * 2) % MOD