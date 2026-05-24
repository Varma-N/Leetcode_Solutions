class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ['a'] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        
        # Place str2 at all 'T' positions
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if fixed[idx] and ans[idx] != str2[j]:
                        return ""
                    ans[idx], fixed[idx] = str2[j], True
        
        # Build KMP LPS array
        lps = [0] * m
        k = 0
        for i in range(1, m):
            while k and str2[k] != str2[i]:
                k = lps[k-1]
            k += str2[k] == str2[i]
            lps[i] = k
        
        # Scan and fix 'F' violations
        k = 0
        last_free = -1
        for i in range(n + m - 1):
            if not fixed[i]:
                last_free = i
            
            # KMP match
            while k and (k == m or str2[k] != ans[i]):
                k = lps[k-1]
            k += str2[k] == ans[i]
            
            # Check constraint
            if i >= m - 1:
                start = i - m + 1
                if start < n:
                    if str1[start] == 'T' and k < m:
                        return ""
                    if str1[start] == 'F' and k == m:
                        if last_free < start:
                            return ""
                        ans[last_free] = 'b'
                        # Recompute KMP state from start of current window
                        k = 0
                        for j in range(start, i + 1):
                            while k and (k == m or str2[k] != ans[j]):
                                k = lps[k-1]
                            k += str2[k] == ans[j]
                        last_free -= 1
        
        return "".join(ans)
