class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[r][c] will store [max_score, path_count]
        # Initialize with [-1, 0] to represent unreachable states
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: Starting point 'S' at the bottom-right
        dp[n-1][n-1] = [0, 1]
        
        # Iterate backwards from the bottom-right to the top-left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip the starting point since it's already initialized
                if r == n - 1 and c == n - 1:
                    continue
                # Skip obstacles
                if board[r][c] == 'X':
                    continue
                
                max_score = -1
                paths = 0
                
                # Check the three possible moves: down, right, down-right
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < n and nc < n and dp[nr][nc][0] != -1:
                        next_score, next_paths = dp[nr][nc]
                        
                        if next_score > max_score:
                            max_score = next_score
                            paths = next_paths
                        elif next_score == max_score:
                            paths = (paths + next_paths) % MOD
                
                # If this cell is reachable from at least one valid path
                if max_score != -1:
                    # 'E' counts as 0 extra points, numeric cells add their value
                    current_val = 0 if board[r][c] == 'E' else int(board[r][c])
                    dp[r][c] = [max_score + current_val, paths]
        
        # The result at the destination 'E' (top-left corner)
        ans_score, ans_paths = dp[0][0]
        
        # If it's unreachable, return [0, 0]
        if ans_score == -1:
            return [0, 0]
            
        return [ans_score, ans_paths]