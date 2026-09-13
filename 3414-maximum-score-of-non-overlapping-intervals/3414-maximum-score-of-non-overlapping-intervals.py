from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store intervals as (r, l, weight, original_index)
        sorted_intervals = sorted(
            (intervals[i][1], intervals[i][0], intervals[i][2], i) 
            for i in range(n)
        )
        
        # Extract sorted end times for binary search
        end_times = [interval[0] for interval in sorted_intervals]
        
        # dp[k][i] will store the best state using up to k intervals considering first i intervals
        # State representation: (max_weight, lexicographically_smallest_index_list)
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]
        
        for i in range(1, n + 1):
            r, l, weight, orig_idx = sorted_intervals[i - 1]
            
            # Find the largest index `prev` such that sorted_intervals[prev][0] < l
            # end_times is 0-indexed, so bisect_right with l - 1 gives 1-based index `prev`
            prev = bisect_right(end_times, l - 1)
            
            for k in range(1, 5):
                # Option 1: Do not pick the current interval
                w1, ans1 = dp[k][i - 1]
                
                # Option 2: Pick the current interval
                prev_w, prev_ans = dp[k - 1][prev]
                w2 = prev_w + weight
                ans2 = sorted(prev_ans + [orig_idx])
                
                # Choose the option with higher weight, or lexicographically smaller indices on tie
                if w2 > w1 or (w2 == w1 and ans2 < ans1):
                    dp[k][i] = (w2, ans2)
                else:
                    dp[k][i] = (w1, ans1)
                    
        return dp[4][n][1]