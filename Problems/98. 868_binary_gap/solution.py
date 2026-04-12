class Solution:
    def binaryGap(self, n: int) -> int:
        last_index = -1
        current_index = 0
        max_distance = 0

        while n > 0:
            if n & 1:
                if last_index != -1:
                    distance = current_index - last_index
                    if distance > max_distance:
                        max_distance = distance
                last_index = current_index
            n >>= 1
            current_index += 1

        return max_distance
        
