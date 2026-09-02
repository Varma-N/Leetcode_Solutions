class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        components = [0] * n
        curr_comp = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_comp += 1
            components[i] = curr_comp
            
        return [components[u] == components[v] for u, v in queries]
