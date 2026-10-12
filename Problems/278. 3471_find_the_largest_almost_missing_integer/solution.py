class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        res = {}
        for i in range(0, len(nums)-k+1):
            sub_array_set = list(set(nums[i:i+k]))
            for j in sub_array_set:
                res[j] = res.get(j, 0) + 1
        target_value = 1
        return (max((k for k, v in res.items() if v == target_value), default = -1))