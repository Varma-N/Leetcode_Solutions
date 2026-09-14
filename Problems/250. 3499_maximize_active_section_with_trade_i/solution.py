class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        t = '1' + s + '1'
        
        ones = []
        zeros = []
        
        count = 1
        current_char = '1'
        
        for i in range(1, len(t)):
            if t[i] == current_char:
                count += 1
            else:
                if current_char == '1':
                    ones.append(count)
                    current_char = '0'
                else:
                    zeros.append(count)
                    current_char = '1'
                count = 1
                
        ones.append(count)
        
        if len(ones) <= 2:
            return total_ones
            
        max_z = max(zeros)
        ans = total_ones
        
        for i in range(1, len(ones) - 1):
            sacrificed = ones[i]
            merged_zeros = zeros[i - 1] + ones[i] + zeros[i]
            best_zero = max(merged_zeros, max_z)
            current_total = total_ones - sacrificed + best_zero
            
            if current_total > ans:
                ans = current_total
                
        return ans