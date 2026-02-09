class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # Initialize dp with very small values
        dp = [[-10**9] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i-1] * nums2[j-1]
                # Four choices:
                # 1. Just take current product
                # 2. Take current product + best from previous (i-1, j-1)
                # 3. Skip current nums1 element
                # 4. Skip current nums2 element
                dp[i][j] = max(
                    product,
                    dp[i-1][j-1] + product,
                    dp[i-1][j],
                    dp[i][j-1]
                )
        
        return dp[m][n]
