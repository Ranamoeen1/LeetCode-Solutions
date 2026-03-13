class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Binary search boundaries
        left, right = 1, max(workerTimes) * (mountainHeight * (mountainHeight + 1) // 2)
        
        while left < right:
            mid = (left + right) // 2
            
            # Check if it's possible to reduce mountain height in 'mid' seconds
            total_height = 0
            for t in workerTimes:
                # Solve: t * (x*(x+1)/2) ≤ mid
                # Using quadratic formula: x² + x - 2*mid/t ≤ 0
                # x = (-1 + √(1 + 8*mid/t)) / 2
                max_x = int((-1 + math.sqrt(1 + 8 * mid // t)) // 2)
                total_height += max_x
                
                # Early exit if we already have enough height reduction
                if total_height >= mountainHeight:
                    break
            
            if total_height >= mountainHeight:
                right = mid
            else:
                left = mid + 1
        
        return left