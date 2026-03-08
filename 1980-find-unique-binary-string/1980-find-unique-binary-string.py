class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        
        # Construct a string that differs from each string at position i
        for i in range(n):
            # Take the opposite of the i-th character in the i-th string
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
        
        return ''.join(result)