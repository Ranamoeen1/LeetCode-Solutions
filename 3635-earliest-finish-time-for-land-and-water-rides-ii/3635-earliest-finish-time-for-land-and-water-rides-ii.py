class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Calculate the earliest absolute finish time for any single land ride
        min_land_finish = min(s + d for s, d in zip(landStartTime, landDuration))
        
        # Calculate the earliest absolute finish time for any single water ride
        min_water_finish = min(s + d for s, d in zip(waterStartTime, waterDuration))
        
        ans = float('inf')
        
        # Scenario 1: Land Ride first, then Water Ride
        # We pair the best land ride finish with each water ride
        for s, d in zip(waterStartTime, waterDuration):
            current_finish = max(min_land_finish, s) + d
            if current_finish < ans:
                ans = current_finish
                
        # Scenario 2: Water Ride first, then Land Ride
        # We pair the best water ride finish with each land ride
        for s, d in zip(landStartTime, landDuration):
            current_finish = max(min_water_finish, s) + d
            if current_finish < ans:
                ans = current_finish
                
        return ans