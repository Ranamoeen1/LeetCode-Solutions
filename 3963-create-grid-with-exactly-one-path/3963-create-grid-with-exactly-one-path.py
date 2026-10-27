class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            row = []
            for j in range(n):
                if j == 0 or i == m - 1:
                    row.append('.')
                else:
                    row.append('#')
            grid.append("".join(row))
        return grid