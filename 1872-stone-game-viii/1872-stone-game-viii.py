from typing import List
from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = list(accumulate(stones))
        
        # Base case: taking all stones (index n-1)
        dp = prefix[-1]
        
        # Iterate backwards from index n-2 down to 1
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
            
        return dp