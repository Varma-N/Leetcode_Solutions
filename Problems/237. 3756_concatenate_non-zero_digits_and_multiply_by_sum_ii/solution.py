class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        count = [0] * (m + 1)
        sum_d = [0] * (m + 1)
        val = [0] * (m + 1)
        
        for i in range(1, m + 1):
            d = int(s[i-1])
            if d > 0:
                count[i] = count[i-1] + 1
                sum_d[i] = sum_d[i-1] + d
                val[i] = (val[i-1] * 10 + d) % MOD
            else:
                count[i] = count[i-1]
                sum_d[i] = sum_d[i-1]
                val[i] = val[i-1]
                
        ans = []
        
        for l, r in queries:
            L = l + 1
            R = r + 1
            
            C = count[R] - count[L-1]
            
            if C == 0:
                ans.append(0)
            else:
                X = (val[R] - val[L-1] * pow10[C]) % MOD
                X = (X + MOD) % MOD 
                
                S = sum_d[R] - sum_d[L-1]
                
                ans.append((X * S) % MOD)
                
        return ans