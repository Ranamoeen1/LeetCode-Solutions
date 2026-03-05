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


# class Solution:
#     def minOperations(self, s: str) -> int:
#         count = 0
        
#         for i in range(len(s)):
#             # For pattern starting with '0', at even index we need '0'
#             if i % 2 == 0:
#                 if s[i] == '0':
#                     # Counts for pattern starting with '1' increase
#                     count += 1
#             else:  # i % 2 == 1
#                 if s[i] == '1':
#                     # Counts for pattern starting with '1' increase
#                     count += 1
        
#         # count represents operations needed for pattern starting with '1'
#         # So operations for pattern starting with '0' is n - count
#         return min(count, len(s) - count)


# class Solution:
#     def minOperations(self, s: str) -> int:
#         n = len(s)
#         count1 = 0  # operations for pattern starting with '0'
        
#         for i in range(n):
#             # Convert character to integer (0 or 1)
#             current = ord(s[i]) - ord('0')
            
#             # For pattern starting with '0', expected value is i % 2
#             expected = i % 2
            
#             if current != expected:
#                 count1 += 1
        
#         count2 = n - count1
#         return min(count1, count2)



# class Solution:
#     def minOperations(self, s: str) -> int:
#         n = len(s)
        
#         # Count mismatches for pattern starting with '0'
#         count = sum(1 for i, ch in enumerate(s) 
#                     if (i % 2 == 0 and ch != '0') or (i % 2 == 1 and ch != '1'))
        
#         return min(count, n - count)


