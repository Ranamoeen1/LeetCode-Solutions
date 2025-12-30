class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def is_magic(r, c):
            if grid[r + 1][c + 1] != 5:
                return False

            seen = set()

            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9:
                        return False
                    seen.add(val)

            if len(seen) != 9:
                return False

            for i in range(3):
                if sum(grid[r + i][c:c + 3]) != 15:
                    return False
                if sum(grid[r + j][c + i] for j in range(3)) != 15:
                    return False

            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15:
                return False

            return True

        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1

        return count
