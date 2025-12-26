class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current_penalty = customers.count('Y')
        min_penalty = current_penalty
        earliest_hour = 0
        n = len(customers)
        for i in range(n):
            if customers[i] == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                earliest_hour = i + 1
        return earliest_hour
