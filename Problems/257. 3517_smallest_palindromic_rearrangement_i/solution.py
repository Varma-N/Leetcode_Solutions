from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        
        left_half = []
        mid = ""
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in counts:
                if counts[char] % 2 != 0:
                    mid = char
                
                left_half.append(char * (counts[char] // 2))
                
        left_string = "".join(left_half)
        return left_string + mid + left_string[::-1]