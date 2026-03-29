class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 1  # Single character is always balanced
        
        # Try every starting index
        for start in range(n):
            freq = [0] * 26  # Fixed-size frequency array for 26 letters
            
            # Extend substring to the right
            for end in range(start, n):
                # Update frequency for current character
                idx = ord(s[end]) - ord('a')
                freq[idx] += 1
                
                # Skip check if we can't possibly beat current max_len
                if end - start + 1 <= max_len:
                    continue
                
                # Find min/max among non-zero frequencies
                min_freq = float('inf')
                max_freq = 0
                distinct = 0
                
                for count in freq:
                    if count > 0:
                        distinct += 1
                        min_freq = min(min_freq, count)
                        max_freq = max(max_freq, count)
                
                # Balanced if all non-zero frequencies are equal
                if min_freq == max_freq:
                    max_len = end - start + 1
        
        return max_len

            
