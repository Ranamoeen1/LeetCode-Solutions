class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        
        row_sums = [sum(row) for row in grid]
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]
                
        # Precompute the range of rows and columns each value occupies
        # This allows O(1) existence checks for blocks
        first_row = {}
        last_row = {}
        first_col = {}
        last_col = {}
        
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val not in first_row:
                    first_row[val] = r
                    first_col[val] = c
                first_row[val] = min(first_row[val], r)
                last_row[val] = max(last_row.get(val, r), r)
                first_col[val] = min(first_col[val], c)
                last_col[val] = max(last_col.get(val, c), c)

        def check_h(target_diff, r_start, r_end):
            if target_diff == 0: return True
            if target_diff < 0 or target_diff not in first_row: return False
            
            h = r_end - r_start + 1
            # For a horizontal cut, the width is always 'n'
            if h == 1 and n == 1: return False # 1x1 case
            
            if h == 1: # Horizontal strip
                return grid[r_start][0] == target_diff or grid[r_start][n-1] == target_diff
            if n == 1: # Vertical strip
                return grid[r_start][0] == target_diff or grid[r_end][0] == target_diff
            
            # Multi-row/col block: target just needs to exist in the row range
            return first_row[target_diff] <= r_end and last_row[target_diff] >= r_start

        def check_v(target_diff, c_start, c_end):
            if target_diff == 0: return True
            if target_diff < 0 or target_diff not in first_col: return False
            
            w = c_end - c_start + 1
            # For a vertical cut, the height is always 'm'
            if w == 1 and m == 1: return False
            
            if w == 1: # Vertical strip
                return grid[0][c_start] == target_diff or grid[m-1][c_start] == target_diff
            if m == 1: # Horizontal strip
                return grid[0][c_start] == target_diff or grid[0][c_end] == target_diff
            
            # Block: target just needs to exist in the column range
            return first_col[target_diff] <= c_end and last_col[target_diff] >= c_start

        # --- Try Horizontal Cuts ---
        top_sum = 0
        for r in range(m - 1):
            top_sum += row_sums[r]
            bot_sum = total_sum - top_sum
            if check_h(top_sum - bot_sum, 0, r): return True
            if check_h(bot_sum - top_sum, r + 1, m - 1): return True

        # --- Try Vertical Cuts ---
        left_sum = 0
        for c in range(n - 1):
            left_sum += col_sums[c]
            right_sum = total_sum - left_sum
            if check_v(left_sum - right_sum, 0, c): return True
            if check_v(right_sum - left_sum, c + 1, n - 1): return True

        return False