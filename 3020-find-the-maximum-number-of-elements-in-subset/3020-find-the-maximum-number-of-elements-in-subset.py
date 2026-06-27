from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 1  # Minimum possible subset length is always 1
        
        # Handle the special case of 1s
        if 1 in count:
            ones_count = count[1]
            # The length must be odd, so if it's even, take ones_count - 1
            max_len = max(max_len, ones_count if ones_count % 2 != 0 else ones_count - 1)
        
        # Process other numbers
        for x in count:
            if x == 1:
                continue
                
            # Only start a chain if x is not a perfect square that we could have processed from its root.
            # This is an optimization, though checking every x works fine too.
            current_len = 0
            curr = x
            
            while curr in count and count[curr] >= 2:
                current_len += 2
                curr = curr * curr
                
            # Now curr is either not in count, or has exactly 1 copy
            if curr in count and count[curr] >= 1:
                current_len += 1
            else:
                # If it's not in count, the previous element had to act as the peak instead of an edge
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len