import math
from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        half_counts = {}
        mid = ""
        
        for char in counts:
            if counts[char] % 2 != 0:
                mid = char
            if counts[char] >= 2:
                half_counts[char] = counts[char] // 2
                
        N = sum(half_counts.values())
        
        T = math.factorial(N)
        for count in half_counts.values():
            T //= math.factorial(count)
            
        if k > T:
            return ""
            
        half_str = []
        chars = sorted(half_counts.keys())
        
        for i in range(N, 0, -1):
            for char in chars:
                if half_counts[char] > 0:
                    M = T * half_counts[char] // i
                    if k <= M:
                        half_str.append(char)
                        half_counts[char] -= 1
                        T = M
                        break
                    else:
                        k -= M
                        
        half_res = "".join(half_str)
        return half_res + mid + half_res[::-1]
        