class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for p in nums:
            # Case where it's impossible
            if p == 2:
                ans.append(-1)
                continue

            # Count trailing 1s in binary representation of p
            t = 0
            temp = p
            while temp & 1:
                t += 1
                temp >>= 1

            # Smallest x such that x OR (x + 1) == p
            x = p - (1 << (t - 1))
            ans.append(x)

        return ans
