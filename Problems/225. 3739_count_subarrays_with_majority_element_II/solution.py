class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = [0] * (2 * n + 2)
        offset = n
        count[offset] = 1
        curr_sum = 0
        smaller_count = 0
        ans = 0
        
        for num in nums:
            if num == target:
                smaller_count += count[curr_sum + offset]
                curr_sum += 1
            else:
                smaller_count -= count[curr_sum - 1 + offset]
                curr_sum -= 1
                
            ans += smaller_count
            count[curr_sum + offset] += 1
            
        return ans