class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends_with = [0] * 26
        total = 0
        
        for char in s:
            idx = ord(char) - ord('a')
            old_val = ends_with[idx]
            ends_with[idx] = (total + 1) % MOD
            total = (total + ends_with[idx] - old_val) % MOD
            
        return total