class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        
        # Booth's Algorithm to find the lexicographically minimal cyclic shift
        def get_min_rotation(arr):
            k_len = len(arr)
            double_arr = arr + arr
            i = 0
            j = 1
            k = 0
            while i < k_len and j < k_len and k < k_len:
                a = double_arr[i + k]
                b = double_arr[j + k]
                if a == b:
                    k += 1
                elif a > b:
                    i += k + 1
                    if i <= j:
                        i = j + 1
                    k = 0
                else:
                    j += k + 1
                    if j <= i:
                        j = i + 1
                    k = 0
            start = min(i, j)
            return arr[start:] + arr[:start]

        # Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        total_sum = 0
        
        for k in divisors:
            valid = True
            for i in range(0, n, k):
                block = nums[i:i+k]
                target = s[i:i+k]
                
                if get_min_rotation(block) != target:
                    valid = False
                    break
            
            if valid:
                total_sum += k
                
        return total_sum



# class Solution:
#     def sortableIntegers(self, nums: list[int]) -> int:
#         n = len(nums)
#         s = sorted(nums)
        
#         # Helper function to find the lexicographically minimal cyclic shift (Booth's Algorithm)
#         def get_min_rotation(arr):
#             k_len = len(arr)
#             double_arr = arr + arr
#             i = 0
#             j = 1
#             k = 0
#             while i < k_len and j < k_len and k < k_len:
#                 if double_arr[i + k] == double_arr[j + k]:
#                     k += 1
#                 elif double_arr[i + k] > double_arr[j + k]:
#                     i = i + k + 1
#                     if i <= j:
#                         i = j + 1
#                     k = 0
#                 else:
#                     j = j + k + 1
#                     if j <= i:
#                         j = i + 1
#                     k = 0
#             start = min(i, j)
#             return arr[start:] + arr[:start]

#         # Find all divisors of n
#         divisors = []
#         for i in range(1, int(n**0.5) + 1):
#             if n % i == 0:
#                 divisors.append(i)
#                 if i * i != n:
#                     divisors.append(n // i)
        
#         total_sum = 0
        
#         for k in divisors:
#             valid = True
#             for i in range(0, n, k):
#                 block = nums[i:i+k]
#                 target = s[i:i+k]
                
#                 # Check if the minimum rotation of the block matches the sorted target
#                 if get_min_rotation(block) != target:
#                     valid = False
#                     break
            
#             if valid:
#                 total_sum += k
                
#         return total_sum



# # class Solution:
# #     def sortableIntegers(self, nums: list[int]) -> int:
# #         n = len(nums)
# #         s = sorted(nums)
        
# #         # Find all divisors of n
# #         divisors = []
# #         for i in range(1, int(n**0.5) + 1):
# #             if n % i == 0:
# #                 divisors.append(i)
# #                 if i * i != n:
# #                     divisors.append(n // i)
        
# #         total_sum = 0
        
# #         for k in divisors:
# #             valid = True
# #             for i in range(0, n, k):
# #                 block = nums[i:i+k]
# #                 target = s[i:i+k]
                
# #                 block_str = ''.join(f',{x}' for x in block)
# #                 target_str = ''.join(f',{x}' for x in target)
                
# #                 if target_str not in (block_str + block_str):
# #                     valid = False
# #                     break
            
# #             if valid:
# #                 total_sum += k
                
# #         return total_sum