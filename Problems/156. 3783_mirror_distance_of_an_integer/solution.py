class Solution:
    def mirrorDistance(self, n: int) -> int:
        def rev(num):
            r = 0
            while num > 0:
                r = r * 10 + (num % 10)
                num = num // 10
            return r
        return abs(n - rev(n))
