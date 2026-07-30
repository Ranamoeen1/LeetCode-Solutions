class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        # Calculate pushes based on batches of 8 keys
        first_batch = min(n, 8)
        second_batch = min(max(0, n - 8), 8)
        third_batch = min(max(0, n - 16), 8)
        fourth_batch = max(0, n - 24)
        
        return (first_batch * 1) + (second_batch * 2) + (third_batch * 3) + (fourth_batch * 4)