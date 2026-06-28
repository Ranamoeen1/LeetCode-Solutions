class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Step 1: Sort the array to easily handle the rearrangement condition
        arr.sort()
        
        # Step 2: The first element must always be 1
        arr[0] = 1
        
        # Step 3: Iterate through the array and ensure the adjacent difference condition is met
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
                
        # The maximum element will be the last element after the operations
        return arr[-1]