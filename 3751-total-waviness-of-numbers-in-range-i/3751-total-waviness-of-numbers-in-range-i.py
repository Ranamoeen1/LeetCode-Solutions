class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)
            
            # Any number with fewer than 3 digits has a waviness of 0
            if n < 3:
                continue
                
            # Check every middle digit to see if it's a peak or a valley
            for i in range(1, n - 1):
                prev_digit = s[i - 1]
                curr_digit = s[i]
                next_digit = s[i + 1]
                
                # Check for Peak
                if curr_digit > prev_digit and curr_digit > next_digit:
                    total_waviness += 1
                # Check for Valley
                elif curr_digit < prev_digit and curr_digit < next_digit:
                    total_waviness += 1
                    
        return total_waviness