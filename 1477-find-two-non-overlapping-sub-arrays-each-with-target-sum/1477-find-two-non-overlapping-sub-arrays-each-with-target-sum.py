class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # best_len[i] stores the minimum length of a sub-array with sum == target
        # ending at or before index i.
        INF = float('inf')
        best_len = [INF] * n
        
        # Maps prefix_sum -> index where that sum occurred
        prefix_map = {0: -1}
        
        current_sum = 0
        min_total_len = INF
        min_sub_len = INF
        
        for i, val in enumerate(arr):
            current_sum += val
            prefix_map[current_sum] = i
            
            # Check if there exists a subarray ending at index i with sum == target
            needed = current_sum - target
            if needed in prefix_map:
                start_idx = prefix_map[needed]
                curr_len = i - start_idx
                
                # If there's a valid non-overlapping subarray to the left
                if start_idx >= 0 and best_len[start_idx] != INF:
                    min_total_len = min(min_total_len, curr_len + best_len[start_idx])
                
                min_sub_len = min(min_sub_len, curr_len)
            
            best_len[i] = min_sub_len

        return min_total_len if min_total_len != INF else -1




# class Solution:
#     def minSumOfLengths(self, arr: list[int], target: int) -> int:
#         n = len(arr)
#         # min_len[i] stores the minimum length of a sub-array with sum == target
#         # that ends at or before index i.
#         min_len = [float('inf')] * n
        
#         ans = float('inf')
#         current_sum = 0
#         l = 0
        
#         for r in range(n):
#             current_sum += arr[r]
            
#             # Shrink window from the left if current sum exceeds target
#             while current_sum > target and l <= r:
#                 current_sum -= arr[l]
#                 l += 1
            
#             # When we find a valid sub-array arr[l...r]
#             if current_sum == target:
#                 current_len = r - l + 1
                
#                 # Check if there is a non-overlapping valid sub-array to the left
#                 if l > 0 and min_len[l - 1] != float('inf'):
#                     ans = min(ans, current_len + min_len[l - 1])
                
#                 # Update min_len for the current index r
#                 if r > 0:
#                     min_len[r] = min(min_len[r - 1], current_len)
#                 else:
#                     min_len[r] = current_len
#             else:
#                 # Carry forward the minimum length seen so far
#                 if r > 0:
#                     min_len[r] = min_len[r - 1]
                    
#         return ans if ans != float('inf') else -1