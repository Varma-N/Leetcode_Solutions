class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            A = min(nums[i], nums[n - 1 - i])
            B = max(nums[i], nums[n - 1 - i])
            delta[A + 1] -= 1
            delta[A + B] -= 1
            delta[A + B + 1] += 1
            delta[B + limit + 1] += 1
        curr_moves = n
        min_moves = n
        for x in range(2, 2 * limit + 1):
            curr_moves += delta[x]
            if curr_moves < min_moves:
                min_moves = curr_moves
                
        return min_moves
