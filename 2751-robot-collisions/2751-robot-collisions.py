class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Create list of (position, original_index, health, direction)
        robots = []
        for i in range(n):
            robots.append((positions[i], i, healths[i], directions[i]))
        
        # Sort by position to process left to right
        robots.sort()
        
        # Stack for R robots: [original_index, health]
        stack = []
        
        # Track final health for each robot (0 means dead)
        final_health = [0] * n
        
        for pos, idx, health, direc in robots:
            if direc == 'R':
                stack.append([idx, health])
            else:
                # L robot, process collisions with R robots in stack
                cur_health = health
                
                while stack and cur_health > 0:
                    top_idx, top_health = stack[-1]
                    
                    if top_health > cur_health:
                        # R robot survives, L robot dies
                        stack[-1][1] -= 1
                        cur_health = 0
                    elif top_health < cur_health:
                        # L robot survives this collision, R robot dies
                        stack.pop()
                        cur_health -= 1
                    else:
                        # Both die (equal health)
                        stack.pop()
                        cur_health = 0
                
                # If L robot survived all collisions
                if cur_health > 0:
                    final_health[idx] = cur_health
        
        # R robots in stack survived
        for idx, health in stack:
            final_health[idx] = health
        
        # Return healths of survivors in original order
        return [h for h in final_health if h > 0]