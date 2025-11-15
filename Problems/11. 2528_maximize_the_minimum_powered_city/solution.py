from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Step 1: Compute initial power using sliding window
        power = [0] * n
        curr = 0
        
        # Initial window for city 0
        for i in range(min(n, r + 1)):
            curr += stations[i]
        power[0] = curr
        
        # Slide window for cities 1..n-1
        for i in range(1, n):
            if i - r - 1 >= 0:
                curr -= stations[i - r - 1]
            if i + r < n:
                curr += stations[i + r]
            power[i] = curr

        # Step 2: Binary search for maximum achievable minimum power
        left, right = min(power), max(power) + k
        ans = left

        def canAchieve(target: int) -> bool:
            add = [0] * (n + 1)  # difference array
            curr_add = 0
            used = 0

            for i in range(n):
                curr_add += add[i]
                current_total = power[i] + curr_add

                if current_total < target:
                    need = target - current_total
                    used += need
                    if used > k:
                        return False

                    curr_add += need
                    pos = i + r
                    end = pos + r + 1
                    if end < n:
                        add[end] -= need

            return True

        while left <= right:
            mid = (left + right) // 2
            if canAchieve(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
