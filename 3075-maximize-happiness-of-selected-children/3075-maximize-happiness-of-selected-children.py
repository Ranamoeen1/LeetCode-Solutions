class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        total_happiness = 0
        for i in range(k):
            current_val = max(0, happiness[i] - i)
            total_happiness += current_val
            
        return total_happiness
