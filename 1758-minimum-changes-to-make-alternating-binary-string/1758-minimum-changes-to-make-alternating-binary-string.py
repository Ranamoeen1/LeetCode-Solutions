class Solution:
    def minOperations(self, s: str) -> int:
        # Count operations for pattern starting with '0'
        operations_start_with_0 = 0
        
        # Count operations for pattern starting with '1'
        operations_start_with_1 = 0
        
        for i in range(len(s)):
            
            if i % 2 == 0:
                if s[i] != '0':
                    operations_start_with_0 += 1
                else:
                    operations_start_with_1 += 1
            else:  
                if s[i] != '1':
                    operations_start_with_0 += 1
                else:
                    operations_start_with_1 += 1
        
        return min(operations_start_with_0, operations_start_with_1)