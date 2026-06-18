class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the position of the minute hand in degrees
        minute_angle = minutes * 6
        
        # Calculate the position of the hour hand in degrees
        # (hour % 12) handles the 12 o'clock position resetting to 0
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        # Find the absolute difference between the two angles
        diff = abs(hour_angle - minute_angle)
        
        # Return the smaller angle
        return min(diff, 360 - diff)