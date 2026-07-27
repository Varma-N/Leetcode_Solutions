class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land_finish = min(start + dur for start, dur in zip(landStartTime, landDuration))
        min_water_finish = min(start + dur for start, dur in zip(waterStartTime, waterDuration))
        best_land_first = min(
            max(min_land_finish, w_start) + w_dur 
            for w_start, w_dur in zip(waterStartTime, waterDuration)
        )
        best_water_first = min(
            max(min_water_finish, l_start) + l_dur 
            for l_start, l_dur in zip(landStartTime, landDuration)
        )
        return min(best_land_first, best_water_first)

        