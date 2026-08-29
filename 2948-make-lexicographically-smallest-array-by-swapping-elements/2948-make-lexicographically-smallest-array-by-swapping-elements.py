class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Store numbers along with their original indices and sort by value
        sorted_pairs = sorted([(val, idx) for idx, val in enumerate(nums)])
        
        res = [0] * n
        
        # Process element groups that can reach each other
        group_vals = [sorted_pairs[0][0]]
        group_indices = [sorted_pairs[0][1]]
        
        for i in range(1, n):
            val, idx = sorted_pairs[i]
            prev_val = sorted_pairs[i - 1][0]
            
            # If difference exceeds limit, start a new group
            if val - prev_val > limit:
                # Assign sorted values to sorted indices for the completed group
                group_indices.sort()
                for g_val, g_idx in zip(group_vals, group_indices):
                    res[g_idx] = g_val
                
                # Reset group buffers for the new component
                group_vals = [val]
                group_indices = [idx]
            else:
                group_vals.append(val)
                group_indices.append(idx)
        
        # Process the final remaining group
        group_indices.sort()
        for g_val, g_idx in zip(group_vals, group_indices):
            res[g_idx] = g_val
            
        return res