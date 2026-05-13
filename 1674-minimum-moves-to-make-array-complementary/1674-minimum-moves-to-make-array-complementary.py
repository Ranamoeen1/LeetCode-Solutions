class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # diff[x] will store the change in moves required if target sum is x
        # Range is 2 to 2*limit, so size 2*limit + 2 is sufficient
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # For each pair, we assume 2 moves are needed by default for all sums
            # Range [2, 2 * limit]
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # If the target sum falls in [min(a, b) + 1, max(a, b) + limit], 
            # only 1 move is actually needed. Subtract 1 move from the range.
            min_val = min(a, b)
            max_val = max(a, b)
            diff[min_val + 1] -= 1
            diff[max_val + limit + 1] += 1
            
            # If the target sum is exactly a + b, 0 moves are needed.
            # Subtract another 1 move for this specific point.
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        ans = n  # Maximum possible moves is n (2 moves for all n/2 pairs)
        current_moves = 0
        
        # Sweep through the difference array to find the minimum prefix sum
        for i in range(2, 2 * limit + 1):
            current_moves += diff[i]
            if current_moves < ans:
                ans = current_moves
                
        return ans