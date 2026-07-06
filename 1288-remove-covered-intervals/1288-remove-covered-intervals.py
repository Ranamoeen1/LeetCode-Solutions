class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending. If starts are equal, sort by end descending.
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_end = 0
        
        for start, end in intervals:
            # If the current interval's end is covered by the max_end seen so far
            if end <= max_end:
                count += 1
            else:
                # Update the boundary for covering subsequent intervals
                max_end = end
                
        # The remaining intervals is total minus the removed ones
        return len(intervals) - count