class Solution:
    def minimumDistance(self, word: str) -> int:
        # Build coordinate map for each letter on the keyboard
        # Layout: row 0: A-F, row 1: G-L, row 2: M-R, row 3: S-X, row 4: Y-Z
        coords = {}
        for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            row = i // 6
            col = i % 6
            coords[c] = (row, col)
        
        def dist(c1, c2):
            """Manhattan distance between two letters. 0 if either is None (not placed yet)."""
            if c1 is None or c2 is None:
                return 0
            x1, y1 = coords[c1]
            x2, y2 = coords[c2]
            return abs(x1 - x2) + abs(y1 - y2)
        
        # dp[other_pos] = minimum cost where:
        # - one finger just typed word[i-1] (current position)
        # - the other finger is at position 'other_pos' (None means not placed yet)
        dp = {None: 0}  # After typing first char, cost is 0, other finger not placed
        
        for i in range(1, len(word)):
            curr = word[i]
            prev = word[i - 1]
            new_dp = {}
            
            for other_pos, cost in dp.items():
                # Option 1: Move the finger that was at 'prev' to 'curr'
                d = dist(prev, curr)
                new_other = other_pos
                new_cost = cost + d
                if new_other not in new_dp or new_dp[new_other] > new_cost:
                    new_dp[new_other] = new_cost
                
                # Option 2: Move the other finger to 'curr'
                d = dist(other_pos, curr)
                new_other = prev  # The finger at 'prev' becomes the "other" finger
                new_cost = cost + d
                if new_other not in new_dp or new_dp[new_other] > new_cost:
                    new_dp[new_other] = new_cost
            
            dp = new_dp
        
        return min(dp.values())