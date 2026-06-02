class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort costs in descending order to maximize the value of free candies
        cost.sort(reverse=True)
        
        total_cost = 0
        
        for i in range(len(cost)):
            # Every 3rd candy (index 2, 5, 8, etc.) is free, so we skip adding its cost
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
                
        return total_cost