class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        current_max = 0
        
        for num in nums:
            if num > current_max:
                current_max = num
            prefixGcd.append(math.gcd(num, current_max))
            
        prefixGcd.sort()
        
        ans = 0
        n = len(prefixGcd)
        for i in range(n // 2):
            ans += math.gcd(prefixGcd[i], prefixGcd[n - 1 - i])
            
        return ans