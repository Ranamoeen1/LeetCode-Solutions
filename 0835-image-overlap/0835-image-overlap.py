from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Store the coordinates of 1s for both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count the frequency of each translation vector
        offset_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                offset_counts[(r2 - r1, c2 - c1)] += 1
                
        # Return the maximum overlap found (0 if no ones overlap)
        return max(offset_counts.values()) if offset_counts else 0