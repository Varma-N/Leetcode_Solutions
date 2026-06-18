class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        linear_pts = []
        for x, y in points:
            if y == 0:        
                d = x
            elif x == side:     
                d = side + y
            elif y == side:    
                d = 2 * side + (side - x)
            else:             
                d = 3 * side + (side - y)
            linear_pts.append(d)
        
        linear_pts.sort()
        n = len(linear_pts)
        perimeter = 4 * side

        def can_place(dist):
            for i in range(n):
                if linear_pts[i] > linear_pts[0] + dist:
                    break
                
                count = 1
                last_pos = linear_pts[i]
                first_pos = linear_pts[i]
                
                curr_idx = i
                for _ in range(k - 1):
                    target = last_pos + dist
                    idx = bisect_left(linear_pts, target, lo=curr_idx + 1)
                    
                    if idx < n:
                        last_pos = linear_pts[idx]
                        curr_idx = idx
                        count += 1
                    else:
                        target_wrap = target - perimeter
                        idx_wrap = bisect_left(linear_pts, target_wrap)
                        break
                
                if count == k and (first_pos + perimeter - last_pos) >= dist:
                    return True
            return False
        low = 1
        high = side
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans