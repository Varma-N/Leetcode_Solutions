class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(start_pos, direction):
            arr = nums[:]
            n = len(arr)
            curr = start_pos
            dir = direction
            
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir = -dir
                    curr += dir
       
            return all(x == 0 for x in arr)
        
        n = len(nums)
        count = 0
  
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, -1):
                    count += 1
                if simulate(i, 1):
                    count += 1
        return count
