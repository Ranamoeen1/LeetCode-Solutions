# class Solution:
#     def minOperations(self, s: str) -> int:
#         # Count operations for pattern starting with '0'
#         operations_start_with_0 = 0
        
#         # Count operations for pattern starting with '1'
#         operations_start_with_1 = 0
        
#         for i in range(len(s)):
            
#             if i % 2 == 0:
#                 if s[i] != '0':
#                     operations_start_with_0 += 1
#                 else:
#                     operations_start_with_1 += 1
#             else:  
#                 if s[i] != '1':
#                     operations_start_with_0 += 1
#                 else:
#                     operations_start_with_1 += 1
        
#         return min(operations_start_with_0, operations_start_with_1)

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        operations_start_with_0 = 0
        
        for i in range(n):
            # Expected character for pattern starting with '0'
            expected = '0' if i % 2 == 0 else '1'
            
            if s[i] != expected:
                operations_start_with_0 += 1
        
        # The other pattern will need the remaining operations
        operations_start_with_1 = n - operations_start_with_0
        
        return min(operations_start_with_0, operations_start_with_1)