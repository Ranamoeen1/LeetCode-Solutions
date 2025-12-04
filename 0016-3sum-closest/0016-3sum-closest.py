class Solution:
    def threeSumClosest(self, nums, target):
        # Sort the input list first
        nums.sort()
        
        # Initialize the closest sum to a large value
        closest_sum = float('inf')
        
        # Iterate over the list with index i
        for i in range(len(nums) - 2):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Set the left and right pointers
            left, right = i + 1, len(nums) - 1
            
            # Iterate with two pointers (left and right)
            while left < right:
                # Calculate the current sum
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on comparison with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match found
        
        return closest_sum
