class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')
        
        # Check each index in the array
        for i in range(n):
            if words[i] == target:
                # Calculate clockwise distance
                clockwise = (i - startIndex + n) % n
                # Calculate counter-clockwise distance
                counter_clockwise = (startIndex - i + n) % n
                # Take the minimum of both directions for this occurrence
                distance = min(clockwise, counter_clockwise)
                # Update the global minimum
                min_distance = min(min_distance, distance)
        
        return min_distance if min_distance != float('inf') else -1