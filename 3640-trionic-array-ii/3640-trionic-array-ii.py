class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # Use negative infinity for unreachable states
        inf = float('inf')
        
        # inc: max sum of a strictly increasing sequence ending at current index (len >= 2)
        inc = -inf
        # up_down: max sum of a peak (up-down) pattern ending at current index (len >= 3)
        up_down = -inf
        # up_down_up: max sum of a full trionic subarray ending at current index (len >= 4)
        up_down_up = -inf
        
        # Global maximum for the full trionic pattern
        max_ans = -inf
        
        for i in range(1, len(nums)):
            curr = nums[i]
            prev = nums[i-1]
            
            if curr > prev:
                # Part 1: Strictly Increasing
                
                # Update 'up_down_up': 
                # This continues an existing 'up_down_up' OR starts a new 'up' after an 'up_down'.
                if max(up_down, up_down_up) != -inf:
                    next_up_down_up = max(up_down, up_down_up) + curr
                else:
                    next_up_down_up = -inf
                
                # Update 'inc':
                # This continues an existing 'inc' OR starts a new 'inc' using the previous single element.
                next_inc = max(inc, prev) + curr
                
                # A strictly increasing value breaks a 'down' sequence.
                next_up_down = -inf
                
            elif curr < prev:
                # Part 2: Strictly Decreasing
                
                # Update 'up_down':
                # This continues an existing 'up_down' OR starts a 'down' after an 'inc'.
                if max(inc, up_down) != -inf:
                    next_up_down = max(inc, up_down) + curr
                else:
                    next_up_down = -inf
                
                # A strictly decreasing value breaks 'inc' and 'up_down_up' sequences.
                next_inc = -inf
                next_up_down_up = -inf
                
            else:
                # Part 3: Equal (Flat)
                # All strictly increasing/decreasing conditions are broken.
                next_inc = -inf
                next_up_down = -inf
                next_up_down_up = -inf
            
            # Move to the next state
            inc, up_down, up_down_up = next_inc, next_up_down, next_up_down_up
            
            if up_down_up > max_ans:
                max_ans = up_down_up
                
        return int(max_ans)