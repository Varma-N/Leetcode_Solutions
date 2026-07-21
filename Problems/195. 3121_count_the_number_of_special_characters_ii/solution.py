class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            elif char.isupper():
                if char not in first_upper:
                    first_upper[char] = i
                    
        count = 0
        
        for char, last_idx in last_lower.items():
            upper_char = char.upper()
            if upper_char in first_upper:
                if last_idx < first_upper[upper_char]:
                    count += 1
                    
        return count
        