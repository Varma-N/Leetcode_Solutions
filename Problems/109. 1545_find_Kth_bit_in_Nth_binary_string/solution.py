class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip_count = 0
        while n > 1:
            mid = 1 << (n - 1)
            if k == mid:
                return "1" if flip_count % 2 == 0 else "0"
            elif k > mid:
                k = (1 << n) - k
                flip_count += 1
            n -= 1
        return "0" if flip_count % 2 == 0 else "1"


        
