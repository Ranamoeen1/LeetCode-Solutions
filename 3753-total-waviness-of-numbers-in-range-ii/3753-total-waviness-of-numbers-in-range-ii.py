class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(n: int) -> int:
            if n < 3:
                return 0
            
            s = str(n)
            length = len(s)
            memo = {}
            
            def dp(idx: int, prev: int, prev2: int, is_less: bool, is_started: bool):
                # Base case: We have successfully processed all digits
                if idx == length:
                    return 1, 0  # (count of numbers, total waviness sum)
                
                # Check state cache
                state = (idx, prev, prev2, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(s[idx])
                total_count = 0
                total_waviness = 0
                
                for d in range(limit + 1):
                    next_is_less = is_less or (d < limit)
                    next_is_started = is_started or (d > 0)
                    
                    wave_contribution = 0
                    # A digit creates a peak/valley if we have started the number 
                    # AND both previous digits (prev, prev2) are fully real digits.
                    if is_started and prev2 != -1 and prev != -1:
                        if (prev > prev2 and prev > d) or (prev < prev2 and prev < d):
                            wave_contribution = 1
                    
                    if not next_is_started:
                        # Skip leading zeros entirely by passing -1 markers down
                        sub_count, sub_wave = dp(idx + 1, -1, -1, next_is_less, False)
                    else:
                        if not is_started:
                            # 'd' is the literal first digit of our actual number
                            sub_count, sub_wave = dp(idx + 1, d, -1, next_is_less, True)
                        else:
                            # Standard sequence progression
                            sub_count, sub_wave = dp(idx + 1, d, prev, next_is_less, True)
                    
                    total_count += sub_count
                    # Suffix total waviness + contribution multiplied by downstream arrangements
                    total_waviness += sub_wave + (wave_contribution * sub_count)
                
                memo[state] = (total_count, total_waviness)
                return total_count, total_waviness

            # Extract the accumulated waviness sum from the root state tuple
            return dp(0, -1, -1, False, False)[1]

        return solve(num2) - solve(num1 - 1)




# from functools import lru_cache

# class Solution:
#     def totalWaviness(self, num1: int, num2: int) -> int:
        
#         def solve(n: int) -> int:
#             if n <= 0:
#                 return 0
            
#             s = str(n)
#             length = len(s)
            
#             @lru_cache(None)
#             def dp(idx: int, prev: int, prev2: int, is_less: bool, is_started: bool):
#                 # Base case: if we have constructed the full number
#                 if idx == length:
#                     # If the number has at least 3 digits and the last second-to-last 
#                     # digit is a peak/valley, it's already counted during transitions.
#                     return 1, 0
                
#                 limit = 9 if is_less else int(s[idx])
#                 total_count = 0
#                 total_waviness = 0
                
#                 for d in range(limit + 1):
#                     next_is_less = is_less or (d < limit)
#                     next_is_started = is_started or (d > 0)
                    
#                     # Calculate if the PREVIOUS digit (`prev`) becomes a peak or valley
#                     # We can only evaluate `prev` if we have at least 3 digits established:
#                     # `prev2` (at idx-2), `prev` (at idx-1), and the current digit `d` (at idx).
#                     wave_contribution = 0
#                     if is_started and prev2 != -1 and prev != -1:
#                         if prev > prev2 and prev > d:    # Peak
#                             wave_contribution = 1
#                         elif prev < prev2 and prev < d:  # Valley
#                             wave_contribution = 1
                    
#                     # Standard behavior for leading zeros
#                     if not next_is_started:
#                         # We haven't started the number yet (still parsing leading zeros)
#                         sub_count, sub_wave = dp(idx + 1, -1, -1, next_is_less, False)
#                     else:
#                         # We are actively building the number
#                         if not is_started:
#                             # This digit `d` is the very first digit of the number
#                             sub_count, sub_wave = dp(idx + 1, d, -1, next_is_less, True)
#                         else:
#                             # We have already placed at least one digit prior to `d`
#                             sub_count, sub_wave = dp(idx + 1, d, prev, next_is_less, True)
                    
#                     total_count += sub_count
#                     # Total waviness from this branch is the sum of waviness found deeper 
#                     # in the recursion + (wave_contribution * number of valid suffixes)
#                     total_waviness += sub_wave + (wave_contribution * sub_count)
                    
#                 return total_count, total_waviness

#             return dp(0, -1, -1, False, False)[1]

#         return solve(num2) - solve(num1 - 1)