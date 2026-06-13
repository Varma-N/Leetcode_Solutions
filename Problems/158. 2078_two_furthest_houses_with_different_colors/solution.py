class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        for right in range(n-1, 0, -1):
            if colors[right] != colors[0]:
                rmax_dis = right
                break
        for left in range(n - 1):
            if colors[left] != colors[n - 1]:
                lmax_dis = n - 1 - left
                break
        return max(lmax_dis, rmax_dis)


        
