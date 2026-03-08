# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         n = len(nums)
#         result = []
        
#         # Construct a string that differs from each string at position i
#         for i in range(n):
#             # Take the opposite of the i-th character in the i-th string
#             if nums[i][i] == '0':
#                 result.append('1')
#             else:
#                 result.append('0')
        
#         return ''.join(result)


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        num_set = set(nums)
        
        def backtrack(current):
            if len(current) == n:
                candidate = ''.join(current)
                if candidate not in num_set:
                    return candidate
                return None
            
            # Try '0' first
            current.append('0')
            result = backtrack(current)
            if result:
                return result
            current.pop()
            
            # Try '1'
            current.append('1')
            result = backtrack(current)
            if result:
                return result
            current.pop()
            
            return None
        
        return backtrack([])