class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        lcm_list = []
        for i in range(1, 1 << n):
            curr_lcm = 1
            bits = 0
            for j in range(n):
                if (i >> j) & 1:
                    curr_lcm = math.lcm(curr_lcm, coins[j])
                    bits += 1
            lcm_list.append((curr_lcm, 1 if bits % 2 == 1 else -1))
            
        low, high = 1, min(coins) * k
        ans = high
        while low <= high:
            mid = (low + high) // 2
            res = sum(sign * (mid // val) for val, sign in lcm_list)
            
            if res >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans