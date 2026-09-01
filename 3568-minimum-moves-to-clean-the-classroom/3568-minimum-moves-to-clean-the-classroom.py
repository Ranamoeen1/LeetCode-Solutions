from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start = None
        litter_positions = []
        
        # Parse grid to find 'S' and all 'L' positions
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start = (r, c)
                elif cell == 'L':
                    litter_positions.append((r, c))
        
        num_litter = len(litter_positions)
        target_mask = (1 << num_litter) - 1
        
        # Map (r, c) of each litter to its bit index
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        
        # BFS Queue stores tuples: (r, c, mask, current_energy, moves)
        start_r, start_c = start
        initial_mask = 0
        
        # Check if the starting position itself has a litter (edge case check)
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        queue = deque([(start_r, start_c, initial_mask, energy, 0)])
        
        # visited dictionary: (r, c, mask) -> max_remaining_energy
        visited = {}
        visited[(start_r, start_c, initial_mask)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_energy, moves = queue.popleft()
            
            # If all litter items are collected, return total moves
            if mask == target_mask:
                return moves
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Boundary and obstacle check
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1
                    
                    if next_energy < 0:
                        continue
                    
                    next_mask = mask
                    cell_type = classroom[nr][nc]
                    
                    # Reset area restores energy to maximum capacity
                    if cell_type == 'R':
                        next_energy = energy
                    # Collect litter if it's present at cell
                    elif cell_type == 'L':
                        if (nr, nc) in litter_map:
                            next_mask |= (1 << litter_map[(nr, nc)])
                    
                    # State pruning: store only if we reached (nr, nc, next_mask) with higher energy
                    state_key = (nr, nc, next_mask)
                    if state_key not in visited or visited[state_key] < next_energy:
                        visited[state_key] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, moves + 1))
        
        return -1