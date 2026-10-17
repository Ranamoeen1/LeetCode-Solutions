class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper function to compute the sum of digits of a number
        def get_digit_sum(val: int) -> int:
            d_sum = 0
            while val > 0:
                d_sum += val % 10
                val //= 10
            return d_sum

        # Create tuples: (digit_sum, value, original_index)
        arr = []
        for i, val in enumerate(nums):
            arr.append((get_digit_sum(val), val, i))
        
        # Sort based on digit sum, then by value (tie-breaker)
        arr.sort()
        
        # Track visited indices to find permutation cycles
        visited = [False] * n
        min_swaps = 0
        
        for i in range(n):
            # If the element is already in the correct place or visited, skip
            if visited[i] or arr[i][2] == i:
                continue
            
            # Compute the length of the cycle
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]  # Move to original index of element at current position
                cycle_size += 1
            
            if cycle_size > 0:
                min_swaps += (cycle_size - 1)
                
        return min_swaps