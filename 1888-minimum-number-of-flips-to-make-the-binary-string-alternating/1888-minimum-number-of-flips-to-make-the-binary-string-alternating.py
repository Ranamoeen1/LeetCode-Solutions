class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s
        
      
        mismatches0 = 0 
        mismatches1 = 0  
        
        for i in range(n):
            if i % 2 == 0:
                if s2[i] != '0':
                    mismatches0 += 1
                if s2[i] != '1':
                    mismatches1 += 1
            else:
                if s2[i] != '1':
                    mismatches0 += 1
                if s2[i] != '0':
                    mismatches1 += 1
        
        ans = min(mismatches0, mismatches1)
        
        for i in range(1, n):
           
            if (i-1) % 2 == 0:  
                if s2[i-1] != '0':
                    mismatches0 -= 1
                if s2[i-1] != '1':
                    mismatches1 -= 1
            else:
                if s2[i-1] != '1':
                    mismatches0 -= 1
                if s2[i-1] != '0':
                    mismatches1 -= 1
       
            if (i+n-1) % 2 == 0:
                if s2[i+n-1] != '0':
                    mismatches0 += 1
                if s2[i+n-1] != '1':
                    mismatches1 += 1
            else:
                if s2[i+n-1] != '1':
                    mismatches0 += 1
                if s2[i+n-1] != '0':
                    mismatches1 += 1
            
            ans = min(ans, mismatches0, mismatches1)
        
        return ans

# class Solution:
#     def minFlips(self, s: str) -> int:
#         n = len(s)
        
#         # For pattern starting with '0': even indices should be '0', odd indices should be '1'
#         # For pattern starting with '1': even indices should be '1', odd indices should be '0'
        
#         # Count initial mismatches
#         diff0 = 0  # mismatches with pattern starting with '0'
#         diff1 = 0  # mismatches with pattern starting with '1'
        
#         for i in range(n):
#             # Expected char for pattern0 at position i
#             expected0 = '0' if i % 2 == 0 else '1'
#             # Expected char for pattern1 at position i
#             expected1 = '1' if i % 2 == 0 else '0'
            
#             if s[i] != expected0:
#                 diff0 += 1
#             if s[i] != expected1:
#                 diff1 += 1
        
#         min_flips = min(diff0, diff1)
        
#         # For odd length strings, after n rotations, patterns swap
#         if n % 2 == 1:
#             # Slide and update
#             s2 = s + s
#             for i in range(1, n):
#                 # When we rotate, the pattern requirements shift
#                 # We can update by checking the character that moves from front to back
                
#                 # Character that moves from front (position i-1) to back
#                 # At front, it was compared with pattern based on index 0
#                 # At back, it will be compared with pattern based on index n-1
                
#                 # Update diff0
#                 if s2[i-1] != ('0' if (i-1) % 2 == 0 else '1'):
#                     diff0 -= 1
#                 if s2[i+n-1] != ('0' if (i+n-1) % 2 == 0 else '1'):
#                     diff0 += 1
                
#                 # Update diff1
#                 if s2[i-1] != ('1' if (i-1) % 2 == 0 else '0'):
#                     diff1 -= 1
#                 if s2[i+n-1] != ('1' if (i+n-1) % 2 == 0 else '0'):
#                     diff1 += 1
                
#                 min_flips = min(min_flips, diff0, diff1)
        
#         return min_flips

# class Solution:
#     def minFlips(self, s: str) -> int:
#         n = len(s)
#         s2 = s + s
#         alt1, alt2 = '', ''
        
#         # Generate alternating patterns
#         for i in range(2*n):
#             alt1 += '0' if i % 2 == 0 else '1'
#             alt2 += '1' if i % 2 == 0 else '0'
        
#         # Count differences
#         diff1, diff2 = 0, 0
#         result = float('inf')
        
#         # Sliding window
#         for i in range(2*n):
#             if s2[i] != alt1[i]:
#                 diff1 += 1
#             if s2[i] != alt2[i]:
#                 diff2 += 1
            
#             # When window size reaches n, we have a valid rotation
#             if i >= n:
#                 if s2[i-n] != alt1[i-n]:
#                     diff1 -= 1
#                 if s2[i-n] != alt2[i-n]:
#                     diff2 -= 1
            
#             # Update result when we have a complete window
#             if i >= n-1:
#                 result = min(result, diff1, diff2)
        
#         return result