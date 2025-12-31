class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def canCross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1
            
            queue = deque()
            visited = [[False] * col for _ in range(row)]
            
            for j in range(col):
                if grid[0][j] == 0:
                    queue.append((0, j))
                    visited[0][j] = True
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
            
            return False
        
        left, right = 1, row * col
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer