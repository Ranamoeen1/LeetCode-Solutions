class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Efficiently count set bits across all numbers for each position (0 to 30)
        bit_counts = [sum((num >> i) & 1 for num in nums) for i in range(31)]
        
        ans = 0
        # Greedily construct the k largest possible numbers layer by layer
        for _ in range(k):
            curr = 0
            for i in range(31):
                if bit_counts[i] > 0:
                    curr |= (1 << i)
                    bit_counts[i] -= 1
            ans = (ans + curr * curr) % MOD
            
        return ans



# class Solution:
#     def maxSum(self, nums: List[int], k: int) -> int:
#         MOD = 10**9 + 7
#         cnt = [0] * 31
        
#         # Count the number of set bits at each position
#         for x in nums:
#             for i in range(31):
#                 if (x >> i) & 1:
#                     cnt[i] += 1
        
#         ans = 0
#         # Greedily build the k largest possible numbers
#         for _ in range(k):
#             x = 0
#             for i in range(31):
#                 if cnt[i] > 0:
#                     x |= (1 << i)
#                     cnt[i] -= 1
#             ans = (ans + x * x) % MOD
            
#         return ans