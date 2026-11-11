class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Strategy 1: Buy only Type 1 and Type 2 items separately
        a = need1 * cost1 + need2 * cost2
        
        # Strategy 2: Buy only Type 3 items to cover the maximum need
        b = costBoth * max(need1, need2)
        
        # Strategy 3: Buy min(need1, need2) Type 3 items, then cover the remainder with Type 1 or Type 2
        mn = min(need1, need2)
        c = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        
        return min(a, b, c)