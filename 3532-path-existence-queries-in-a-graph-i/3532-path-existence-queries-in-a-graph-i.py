class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Array to store the component ID for each node
        comp = [0] * n
        current_id = 0
        
        # Identify connected components in O(n)
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            comp[i] = current_id
            
        # Process each query in O(1)
        answer = []
        for u, v in queries:
            answer.append(comp[u] == comp[v])
            
        return answer