class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequencies of each character
        freq = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        # Step 3: Calculate cost based on position index
        for i, count in enumerate(sorted_freqs):
            # i // 8 gives 0 for first 8 chars, 1 for next 8, etc.
            pushes_per_char = (i // 8) + 1
            total_pushes += count * pushes_per_char
            
        return total_pushes