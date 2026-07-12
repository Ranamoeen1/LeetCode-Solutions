class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 1. Get unique elements and sort them
        sorted_unique = sorted(set(arr))
        
        # 2. Map each element to its rank (starting from 1)
        ranks = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
        # 3. Replace each element in the original array with its rank
        return [ranks[num] for num in arr]