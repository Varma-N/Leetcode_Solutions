import heapq
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 1
        
        lo = []          # Max-heap (store negatives) for smallest 'need' elements
        hi = []          # Min-heap for remaining elements
        lo_cnt = {}      # Count of valid elements in lo
        hi_cnt = {}      # Count of valid elements in hi
        lo_size = 0      # Valid element count in lo
        hi_size = 0      # Valid element count in hi
        lo_sum = 0       # Sum of elements in lo
        
        hpsh = heapq.heappush
        hpop = heapq.heappop
        
        # Initialize window [1, 1+dist] - add all to hi first
        for i in range(1, dist + 2):
            x = nums[i]
            hi_cnt[x] = hi_cnt.get(x, 0) + 1
            hpsh(hi, x)
            hi_size += 1
        
        # Rebalance: move 'need' smallest elements from hi to lo
        while lo_size < need and hi:
            while hi and hi_cnt.get(hi[0], 0) == 0:
                hpop(hi)
            if not hi:
                break
            y = hpop(hi)
            hi_cnt[y] -= 1
            hi_size -= 1
            hpsh(lo, -y)
            lo_cnt[y] = lo_cnt.get(y, 0) + 1
            lo_size += 1
            lo_sum += y
        
        # Fix ordering between heaps
        while lo and hi:
            while lo and lo_cnt.get(-lo[0], 0) == 0:
                hpop(lo)
            while hi and hi_cnt.get(hi[0], 0) == 0:
                hpop(hi)
            if not lo or not hi:
                break
            if -lo[0] > hi[0]:
                a = -hpop(lo)
                lo_cnt[a] -= 1
                lo_size -= 1
                lo_sum -= a
                b = hpop(hi)
                hi_cnt[b] -= 1
                hi_size -= 1
                hpsh(hi, a)
                hi_cnt[a] = hi_cnt.get(a, 0) + 1
                hi_size += 1
                hpsh(lo, -b)
                lo_cnt[b] = lo_cnt.get(b, 0) + 1
                lo_size += 1
                lo_sum += b
            else:
                break
        
        ans = nums[0] + lo_sum
        nums0 = nums[0]
        
        # Slide window: left boundary from 2 to n-1-dist
        for left in range(2, n - dist):
            # Remove left-1 element
            x_remove = nums[left - 1]
            if lo_cnt.get(x_remove, 0) > 0:
                lo_cnt[x_remove] -= 1
                lo_size -= 1
                lo_sum -= x_remove
            else:
                hi_cnt[x_remove] -= 1
                hi_size -= 1
            
            # Add new element at left+dist
            x_add = nums[left + dist]
            hi_cnt[x_add] = hi_cnt.get(x_add, 0) + 1
            hpsh(hi, x_add)
            hi_size += 1
            
            # Rebalance to maintain exactly 'need' smallest elements in lo
            # 1. Fill lo if under capacity
            while lo_size < need and hi:
                while hi and hi_cnt.get(hi[0], 0) == 0:
                    hpop(hi)
                if not hi:
                    break
                y = hpop(hi)
                hi_cnt[y] -= 1
                hi_size -= 1
                hpsh(lo, -y)
                lo_cnt[y] = lo_cnt.get(y, 0) + 1
                lo_size += 1
                lo_sum += y
            
            # 2. Trim lo if over capacity
            while lo_size > need and lo:
                while lo and lo_cnt.get(-lo[0], 0) == 0:
                    hpop(lo)
                if not lo:
                    break
                y = -hpop(lo)
                lo_cnt[y] -= 1
                lo_size -= 1
                lo_sum -= y
                hpsh(hi, y)
                hi_cnt[y] = hi_cnt.get(y, 0) + 1
                hi_size += 1
            
            # 3. Fix ordering between heaps
            while lo and hi:
                while lo and lo_cnt.get(-lo[0], 0) == 0:
                    hpop(lo)
                while hi and hi_cnt.get(hi[0], 0) == 0:
                    hpop(hi)
                if not lo or not hi:
                    break
                if -lo[0] > hi[0]:
                    a = -hpop(lo)
                    lo_cnt[a] -= 1
                    lo_size -= 1
                    lo_sum -= a
                    b = hpop(hi)
                    hi_cnt[b] -= 1
                    hi_size -= 1
                    hpsh(hi, a)
                    hi_cnt[a] = hi_cnt.get(a, 0) + 1
                    hi_size += 1
                    hpsh(lo, -b)
                    lo_cnt[b] = lo_cnt.get(b, 0) + 1
                    lo_size += 1
                    lo_sum += b
                else:
                    break
            
            total = nums0 + lo_sum
            if total < ans:
                ans = total
        
        return ans
