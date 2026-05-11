from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elements = []

            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            # top row
            for j in range(left, right + 1):
                elements.append(grid[top][j])

            # right column
            for i in range(top + 1, bottom):
                elements.append(grid[i][right])

            # bottom row
            for j in range(right, left - 1, -1):
                elements.append(grid[bottom][j])

            # left column
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            length = len(elements)
            rot = k % length

            # Counter-clockwise rotation
            rotated = elements[rot:] + elements[:rot]

            idx = 0

            # put back top row
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1

            # put back right column
            for i in range(top + 1, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            # put back bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            # put back left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid