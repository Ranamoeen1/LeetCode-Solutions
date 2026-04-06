# class Solution:
#     def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
#         # Directions: north, east, south, west
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         # Initial direction index (0 = north)
#         dir_idx = 0
#         # Initial position
#         x, y = 0, 0
#         # Maximum squared distance
#         max_dist = 0
        
#         # Convert obstacles list to a set for O(1) lookup
#         obstacle_set = set(map(tuple, obstacles))
        
#         # Process each command
#         for cmd in commands:
#             if cmd == -2:  # Turn left
#                 dir_idx = (dir_idx - 1) % 4
#             elif cmd == -1:  # Turn right
#                 dir_idx = (dir_idx + 1) % 4
#             else:  # Move forward
#                 dx, dy = directions[dir_idx]
#                 # Move step by step to handle obstacles
#                 for _ in range(cmd):
#                     next_x, next_y = x + dx, y + dy
#                     # Check if next position is an obstacle
#                     if (next_x, next_y) in obstacle_set:
#                         break  # Stop moving if obstacle encountered
#                     x, y = next_x, next_y
#                     # Update maximum squared distance
#                     max_dist = max(max_dist, x*x + y*y)
        
#         return max_dist

from typing import List
from collections import defaultdict
import bisect

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: north, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start facing north
        x, y = 0, 0
        max_dist = 0
        
        # Group obstacles by row (for horizontal movement) and by column (for vertical movement)
        row_obstacles = defaultdict(list)  # key: y, value: list of x coordinates
        col_obstacles = defaultdict(list)  # key: x, value: list of y coordinates
        
        for ox, oy in obstacles:
            row_obstacles[oy].append(ox)
            col_obstacles[ox].append(oy)
        
        # Sort obstacle lists for binary search
        for key in row_obstacles:
            row_obstacles[key].sort()
        for key in col_obstacles:
            col_obstacles[key].sort()
        
        for cmd in commands:
            if cmd == -2:  # Turn left
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:  # Turn right
                dir_idx = (dir_idx + 1) % 4
            else:  # Move forward k units
                dx, dy = directions[dir_idx]
                
                if dx != 0:  # Moving horizontally (east or west)
                    target_x = x + dx * cmd
                    # Check for obstacles in the current row
                    if y in row_obstacles:
                        obstacles_x = row_obstacles[y]
                        if dx > 0:  # Moving east
                            # Find first obstacle to the right of current position
                            idx = bisect.bisect_right(obstacles_x, x)
                            if idx < len(obstacles_x):
                                next_obstacle = obstacles_x[idx]
                                if next_obstacle <= target_x:
                                    target_x = next_obstacle - 1
                        else:  # Moving west
                            # Find first obstacle to the left of current position
                            idx = bisect.bisect_left(obstacles_x, x) - 1
                            if idx >= 0:
                                next_obstacle = obstacles_x[idx]
                                if next_obstacle >= target_x:
                                    target_x = next_obstacle + 1
                    x = target_x
                    
                else:  # Moving vertically (north or south)
                    target_y = y + dy * cmd
                    # Check for obstacles in the current column
                    if x in col_obstacles:
                        obstacles_y = col_obstacles[x]
                        if dy > 0:  # Moving north
                            idx = bisect.bisect_right(obstacles_y, y)
                            if idx < len(obstacles_y):
                                next_obstacle = obstacles_y[idx]
                                if next_obstacle <= target_y:
                                    target_y = next_obstacle - 1
                        else:  # Moving south
                            idx = bisect.bisect_left(obstacles_y, y) - 1
                            if idx >= 0:
                                next_obstacle = obstacles_y[idx]
                                if next_obstacle >= target_y:
                                    target_y = next_obstacle + 1
                    y = target_y
                
                # Update maximum distance
                max_dist = max(max_dist, x*x + y*y)
        
        return max_dist