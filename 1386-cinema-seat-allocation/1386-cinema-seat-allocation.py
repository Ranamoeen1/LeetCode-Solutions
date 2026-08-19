from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Group reserved seats by row (only tracking seats 2 through 9)
        reserved_map = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_map[row] |= (1 << seat)
        
        # Bitmasks for the three possible 4-seat blocks
        left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)    # Seats 2, 3, 4, 5
        right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)   # Seats 6, 7, 8, 9
        middle_mask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)  # Seats 4, 5, 6, 7
        
        # Unaffected rows (or rows with reservations only on seats 1 or 10) fit 2 groups
        ans = 2 * (n - len(reserved_map))
        
        for mask in reserved_map.values():
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or ((mask & middle_mask) == 0):
                ans += 1
                
        return ans