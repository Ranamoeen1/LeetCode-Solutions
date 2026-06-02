class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish_time = float('inf')
        
        # Iterate through every possible pair of land and water rides
        for i in range(len(landStartTime)):
            l_start = landStartTime[i]
            l_dur = landDuration[i]
            l_end = l_start + l_dur
            
            for j in range(len(waterStartTime)):
                w_start = waterStartTime[j]
                w_dur = waterDuration[j]
                w_end = w_start + w_dur
                
                # Option 1: Land ride first, then Water ride
                finish_option1 = max(l_end, w_start) + w_dur
                
                # Option 2: Water ride first, then Land ride
                finish_option2 = max(w_end, l_start) + l_dur
                
                # Track the absolute minimum finish time seen so far
                min_finish_time = min(min_finish_time, finish_option1, finish_option2)
                
        return min_finish_time