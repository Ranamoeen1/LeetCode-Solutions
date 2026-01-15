class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        h_max = 1
        current = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1] + 1:
                current += 1
            else:
                h_max = max(h_max, current)
                current = 1
        h_max = max(h_max, current)
        
        # Find longest consecutive sequence in vBars
        v_max = 1
        current = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1] + 1:
                current += 1
            else:
                v_max = max(v_max, current)
                current = 1
        v_max = max(v_max, current)
        
        # The side length is the minimum of (h_max + 1) and (v_max + 1)
        # Because removing k consecutive bars creates a gap of (k + 1) units
        side_length = min(h_max + 1, v_max + 1)
        
        return side_length * side_length