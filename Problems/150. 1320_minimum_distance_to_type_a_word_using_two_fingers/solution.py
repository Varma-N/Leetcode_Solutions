class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(char1, char2):
            if char1 == None: return 0
            c1, c2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
        dp = {None: 0}
        
        for i in range(len(word) - 1):
            curr_char, next_char = word[i], word[i+1]
            new_dp = {}
            
            for other_f, cost in dp.items():
                move_active = cost + get_dist(curr_char, next_char)
                new_dp[other_f] = min(new_dp.get(other_f, float('inf')), move_active)
                
                move_other = cost + get_dist(other_f, next_char)
                new_dp[curr_char] = min(new_dp.get(curr_char, float('inf')), move_other)
            
            dp = new_dp
            
        return min(dp.values())
        
