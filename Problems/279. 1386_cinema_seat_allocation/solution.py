class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_map = defaultdict(int)
        
        # Build the bitmask for each row
        # (1 << seat) sets the corresponding bit to 1
        for row, seat in reservedSeats:
            reserved_map[row] |= (1 << seat)
            
        # We start with the assumption that all empty rows can hold 2 groups
        max_groups = (n - len(reserved_map)) * 2
        
        # Bitmasks representing the required seats for each block type
        # Left block (2,3,4,5):   (1<<2)|(1<<3)|(1<<4)|(1<<5) = 60
        # Right block (6,7,8,9):  (1<<6)|(1<<7)|(1<<8)|(1<<9) = 960
        # Middle block (4,5,6,7): (1<<4)|(1<<5)|(1<<6)|(1<<7) = 240
        
        for mask in reserved_map.values():
            # If both left AND right blocks are free
            if (mask & 60) == 0 and (mask & 960) == 0:
                max_groups += 2
            # Otherwise, check if ANY of the three blocks are free
            elif (mask & 60) == 0 or (mask & 960) == 0 or (mask & 240) == 0:
                max_groups += 1
                
        return max_groups