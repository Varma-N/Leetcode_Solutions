class Solution:
    def maximizeSquareHoleArea(
        self,
        n: int,
        m: int,
        hBars: List[int],
        vBars: List[int]
    ) -> int:
        
        def longest_consecutive(bars: List[int]) -> int:
            if not bars:
                return 1
            
            bars.sort()
            longest = 1
            curr = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                longest = max(longest, curr)
            
            return longest + 1
        
        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)
        
        side = min(max_h, max_v)
        return side * side
