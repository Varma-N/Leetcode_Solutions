class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        total_count = 0
        window_counts = {}
        n = len(s)
        
        for right in range(n):
            char_right = s[right]
            window_counts[char_right] = window_counts.get(char_right, 0) + 1
            
            while len(window_counts) == 3:
                total_count += n - right
                
                char_left = s[left]
                window_counts[char_left] -= 1
                if window_counts[char_left] == 0:
                    del window_counts[char_left]
                    
                left += 1
                
        return total_count
        