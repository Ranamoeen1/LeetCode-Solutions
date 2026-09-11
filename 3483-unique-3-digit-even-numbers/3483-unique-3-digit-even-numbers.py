from typing import List
from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        count = 0
        
        # Iterate over all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract individual digits
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            # Count the frequency of required digits for the current number
            req = Counter([d1, d2, d3])
            
            # Check if all required digits can be supplied by `freq`
            if all(freq[digit] >= req_count for digit, req_count in req.items()):
                count += 1
                
        return count