class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: north, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction index (0 = north)
        dir_idx = 0
        # Initial position
        x, y = 0, 0
        # Maximum squared distance
        max_dist = 0
        
        # Convert obstacles list to a set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Process each command
        for cmd in commands:
            if cmd == -2:  # Turn left
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:  # Turn right
                dir_idx = (dir_idx + 1) % 4
            else:  # Move forward
                dx, dy = directions[dir_idx]
                # Move step by step to handle obstacles
                for _ in range(cmd):
                    next_x, next_y = x + dx, y + dy
                    # Check if next position is an obstacle
                    if (next_x, next_y) in obstacle_set:
                        break  # Stop moving if obstacle encountered
                    x, y = next_x, next_y
                    # Update maximum squared distance
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist