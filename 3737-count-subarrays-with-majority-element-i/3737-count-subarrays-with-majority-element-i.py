class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # count_map stores the frequency of each prefix sum encountered
        # We initialize with {0: 1} because a prefix sum of 0 exists before we process any element
        count_map = {0: 1}
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            # Transform target to +1 and everything else to -1
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
            
            # Count all previous prefix sums that are strictly less than current_sum
            for prev_sum, count in count_map.items():
                if prev_sum < current_sum:
                    total_subarrays += count
            
            # Record the current prefix sum into the map
            count_map[current_sum] = count_map.get(current_sum, 0) + 1
            
        return total_subarrays