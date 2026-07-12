class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 1. Sort the unique elements in one step
        # 2. Build the rank lookup dictionary using a generator inside dict()
        ranks = dict(zip(sorted(set(arr)), range(1, len(set(arr)) + 1)))
        
        # 3. Use map() paired with a dictionary .get lookup for fast C-level iteration
        return list(map(ranks.get, arr))



# class Solution:
#     def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         # 1. Get unique elements and sort them
#         sorted_unique = sorted(set(arr))
        
#         # 2. Map each element to its rank (starting from 1)
#         ranks = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
#         # 3. Replace each element in the original array with its rank
#         return [ranks[num] for num in arr]