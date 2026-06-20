class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Base case: building 1 always has height 0
        restrictions.append([1, 0])
        
        # Sort restrictions by building ID
        restrictions.sort()
        
        # If the last building is not restricted, add a placeholder restriction
        if restrictions[-1][0] != n:
            restrictions.append([n, float('inf')])
            
        m = len(restrictions)
        
        # Pass 1: Left to Right propagation
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
            
        # Pass 2: Right to Left propagation
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
            
        # Find the maximum height achieved between any two adjacent restricted buildings
        max_height = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            # Calculate the peak height between these two restricted points
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        return max_height