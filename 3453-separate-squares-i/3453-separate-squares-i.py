class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        low = float('inf')
        high = float('-inf')
        
        for _, y, l in squares:
            total_area += l * l
            low = min(low, y)
            high = max(high, y + l)
        
        target = total_area / 2.0
        
        def below_area(c: float) -> float:
            total = 0.0
            for _, y, l in squares:
                if c <= y:
                    continue
                elif c >= y + l:
                    total += l * l
                else:
                    total += l * (c - y)
            return total
        for _ in range(80):
            mid = (low + high) / 2.0
            if below_area(mid) < target:
                low = mid
            else:
                high = mid
        
        return low