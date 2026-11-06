import bisect
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        intervals_sorted = sorted([(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)])
        starts = [x[0] for x in intervals_sorted]
        
        next_idx = [bisect.bisect_right(starts, intervals_sorted[i][1]) for i in range(n)]
        
        prev_dp = [(0, [])] * (n + 1)
        
        for k in range(1, 5):
            curr_dp = [(0, [])] * (n + 1)
            for i in range(n - 1, -1, -1):
                skip = curr_dp[i + 1]
                
                w, idx = intervals_sorted[i][2], intervals_sorted[i][3]
                prev_w, prev_list = prev_dp[next_idx[i]]
                
                take_list = prev_list[:]
                take_list.append(-idx)
                take_list.sort(reverse=True)
                
                take = (w + prev_w, take_list)
                
                if take > skip:
                    curr_dp[i] = take
                else:
                    curr_dp[i] = skip
            prev_dp = curr_dp
            
        return [-x for x in prev_dp[0][1]]