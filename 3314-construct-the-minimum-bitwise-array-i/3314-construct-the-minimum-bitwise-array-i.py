class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for N in nums:
            if N == 2:
                ans.append(-1)
                continue
            found = -1
            for x in range(N):  
                if (x | (x + 1)) == N:
                    found = x
                    break
            ans.append(found)
        return ans