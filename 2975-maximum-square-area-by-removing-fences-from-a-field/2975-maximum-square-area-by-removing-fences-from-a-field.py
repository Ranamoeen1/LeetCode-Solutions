class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Collect all horizontal lines
        h_lines = [1] + sorted(hFences) + [m]
        v_lines = [1] + sorted(vFences) + [n]
        
        # Step 2: Compute all possible horizontal gaps
        h_gaps = set()
        for i in range(len(h_lines)):
            for j in range(i + 1, len(h_lines)):
                h_gaps.add(h_lines[j] - h_lines[i])
        
        # Step 3: Compute all possible vertical gaps
        v_gaps = set()
        for i in range(len(v_lines)):
            for j in range(i + 1, len(v_lines)):
                v_gaps.add(v_lines[j] - v_lines[i])
        
        # Step 4: Find max common gap
        common_gaps = h_gaps.intersection(v_gaps)
        if not common_gaps:
            return -1
        
        max_side = max(common_gaps)
        return (max_side * max_side) % MOD