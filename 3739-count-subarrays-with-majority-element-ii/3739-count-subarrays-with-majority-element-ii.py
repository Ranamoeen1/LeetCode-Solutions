class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # The prefix sum can range from -n to n. 
        # To avoid negative indices in our Fenwick tree, we shift everything by + (n + 1).
        # Total size needed for Fenwick tree: 2 * n + 2
        offset = n + 1
        bit = [0] * (2 * n + 3)
        
        def update(idx: int, val: int):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        # Initially, PrefixSum = 0 before looking at any elements.
        # We add 1 to the count of PrefixSum = 0 (shifted by offset).
        update(0 + offset, 1)
        
        ans = 0
        current_sum = 0
        
        for num in nums:
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
            
            # We need to find how many previous prefix sums are strictly less than current_sum.
            # In the shifted coordinate, this is strictly less than (current_sum + offset).
            # So we query up to (current_sum + offset - 1).
            ans += query(current_sum + offset - 1)
            
            # Add the current prefix sum to our Fenwick tree tracking
            update(current_sum + offset, 1)
            
        return ans