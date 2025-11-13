from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        fm = defaultdict(int)
        top = SortedList()
        low = SortedList()
        curr = 0

        def change(num: int, count: int):
            nonlocal curr

            prev = (fm[num], num)

            # Remove old state if exists
            if fm[num]:
                if prev in low:
                    low.discard(prev)
                else:
                    top.discard(prev)
                    curr -= fm[num] * num

            # Update frequency
            fm[num] += count

            # Insert new state if still positive
            if fm[num]:
                low.add((fm[num], num))

            # Fill top until it has x elements
            while low and len(top) < x:
                freq, key = low.pop(-1)
                curr += freq * key
                top.add((freq, key))

            # Balance if better candidates exist in low
            while low and top and low[-1] > top[0]:
                freq, key = low.pop(-1)
                xfreq, xkey = top.pop(0)
                curr = curr - xfreq * xkey + freq * key
                low.add((xfreq, xkey))
                top.add((freq, key))

        for i in range(n):
            change(nums[i], 1)
            if i >= k:
                change(nums[i - k], -1)
            if i >= k - 1:
                res.append(curr)

        return res
