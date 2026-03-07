# class Solution:
#     def minFlips(self, s: str) -> int:
#         n = len(s)
#         s2 = s + s
        
      
#         mismatches0 = 0 
#         mismatches1 = 0  
        
#         for i in range(n):
#             if i % 2 == 0:
#                 if s2[i] != '0':
#                     mismatches0 += 1
#                 if s2[i] != '1':
#                     mismatches1 += 1
#             else:
#                 if s2[i] != '1':
#                     mismatches0 += 1
#                 if s2[i] != '0':
#                     mismatches1 += 1
        
#         ans = min(mismatches0, mismatches1)
        
#         for i in range(1, n):
           
#             if (i-1) % 2 == 0:  
#                 if s2[i-1] != '0':
#                     mismatches0 -= 1
#                 if s2[i-1] != '1':
#                     mismatches1 -= 1
#             else:
#                 if s2[i-1] != '1':
#                     mismatches0 -= 1
#                 if s2[i-1] != '0':
#                     mismatches1 -= 1
       
#             if (i+n-1) % 2 == 0:
#                 if s2[i+n-1] != '0':
#                     mismatches0 += 1
#                 if s2[i+n-1] != '1':
#                     mismatches1 += 1
#             else:
#                 if s2[i+n-1] != '1':
#                     mismatches0 += 1
#                 if s2[i+n-1] != '0':
#                     mismatches1 += 1
            
#             ans = min(ans, mismatches0, mismatches1)
        
#         return ans

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        # For pattern starting with '0': even indices should be '0', odd indices should be '1'
        # For pattern starting with '1': even indices should be '1', odd indices should be '0'
        
        # Count initial mismatches
        diff0 = 0  # mismatches with pattern starting with '0'
        diff1 = 0  # mismatches with pattern starting with '1'
        
        for i in range(n):
            # Expected char for pattern0 at position i
            expected0 = '0' if i % 2 == 0 else '1'
            # Expected char for pattern1 at position i
            expected1 = '1' if i % 2 == 0 else '0'
            
            if s[i] != expected0:
                diff0 += 1
            if s[i] != expected1:
                diff1 += 1
        
        min_flips = min(diff0, diff1)
        
        # For odd length strings, after n rotations, patterns swap
        if n % 2 == 1:
            # Slide and update
            s2 = s + s
            for i in range(1, n):
                # When we rotate, the pattern requirements shift
                # We can update by checking the character that moves from front to back
                
                # Character that moves from front (position i-1) to back
                # At front, it was compared with pattern based on index 0
                # At back, it will be compared with pattern based on index n-1
                
                # Update diff0
                if s2[i-1] != ('0' if (i-1) % 2 == 0 else '1'):
                    diff0 -= 1
                if s2[i+n-1] != ('0' if (i+n-1) % 2 == 0 else '1'):
                    diff0 += 1
                
                # Update diff1
                if s2[i-1] != ('1' if (i-1) % 2 == 0 else '0'):
                    diff1 -= 1
                if s2[i+n-1] != ('1' if (i+n-1) % 2 == 0 else '0'):
                    diff1 += 1
                
                min_flips = min(min_flips, diff0, diff1)
        
        return min_flips