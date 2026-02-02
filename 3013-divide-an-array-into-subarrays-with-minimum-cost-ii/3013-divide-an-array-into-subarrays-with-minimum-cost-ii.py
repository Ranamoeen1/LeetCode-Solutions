class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)

        
        target_count = k - 1
       
        left = SortedList()
        right = SortedList()
        current_sum = 0
        
        def add(val):
            nonlocal current_sum
            left.add(val)
            current_sum += val
            if len(left) > target_count:
                removed = left.pop(-1)
                current_sum -= removed
                right.add(removed)
                
        def remove(val):
            nonlocal current_sum
            if val in right:
                right.remove(val)
            else:
                left.remove(val)
                current_sum -= val
                if right:
                    added = right.pop(0)
                    left.add(added)
                    current_sum += added

        for i in range(1, dist + 2):
            add(nums[i])
            
        min_total_cost = current_sum
        
        for i in range(2, n - dist):
            remove(nums[i - 1])
            add(nums[i + dist])
            min_total_cost = min(min_total_cost, current_sum)
            
        return nums[0] + min_total_cost