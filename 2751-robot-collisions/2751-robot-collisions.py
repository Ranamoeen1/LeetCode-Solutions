# class Solution:
#     def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
#         n = len(positions)
        
#         # Create list of (position, original_index, health, direction)
#         robots = []
#         for i in range(n):
#             robots.append((positions[i], i, healths[i], directions[i]))
        
#         # Sort by position to process left to right
#         robots.sort()
        
#         # Stack for R robots: [original_index, health]
#         stack = []
        
#         # Track final health for each robot (0 means dead)
#         final_health = [0] * n
        
#         for pos, idx, health, direc in robots:
#             if direc == 'R':
#                 stack.append([idx, health])
#             else:
#                 # L robot, process collisions with R robots in stack
#                 cur_health = health
                
#                 while stack and cur_health > 0:
#                     top_idx, top_health = stack[-1]
                    
#                     if top_health > cur_health:
#                         # R robot survives, L robot dies
#                         stack[-1][1] -= 1
#                         cur_health = 0
#                     elif top_health < cur_health:
#                         # L robot survives this collision, R robot dies
#                         stack.pop()
#                         cur_health -= 1
#                     else:
#                         # Both die (equal health)
#                         stack.pop()
#                         cur_health = 0
                
#                 # If L robot survived all collisions
#                 if cur_health > 0:
#                     final_health[idx] = cur_health
        
#         # R robots in stack survived
#         for idx, health in stack:
#             final_health[idx] = health
        
#         # Return healths of survivors in original order
#         return [h for h in final_health if h > 0]



# class Solution:
#     def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
#         n = len(positions)
        
#         # Create array of (position, index) and sort to know relative ordering
#         order = sorted(range(n), key=lambda i: positions[i])
        
#         # Stack stores indices of robots moving Right (in order of increasing position)
#         stack = []
        
#         # Current health of each robot (modified during collisions)
#         cur_health = healths.copy()
#         # Whether robot is alive
#         alive = [True] * n
        
#         for idx in order:
#             if directions[idx] == 'R':
#                 # Moving right - might collide with future L robots
#                 stack.append(idx)
#             else:
#                 # Moving left - collide with R robots to its left (in stack)
#                 while stack and alive[idx]:
#                     j = stack[-1]  # R robot with position < positions[idx]
                    
#                     if cur_health[j] > cur_health[idx]:
#                         # R robot wins
#                         cur_health[j] -= 1
#                         alive[idx] = False
#                     elif cur_health[j] < cur_health[idx]:
#                         # L robot wins this round
#                         alive[j] = False
#                         stack.pop()
#                         cur_health[idx] -= 1
#                     else:
#                         # Both die
#                         alive[j] = False
#                         alive[idx] = False
#                         stack.pop()
#                         break
        
#         # Collect survivors in original order
#         result = []
#         for i in range(n):
#             if alive[i]:
#                 result.append(cur_health[i])
        
#         return result


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Sort indices by position
        idx_by_pos = sorted(range(n), key=lambda i: positions[i])
        
        # Stack for R-moving robots (store original index)
        # We use healths array directly, modifying as we go
        health = healths.copy()
        stack = []  # indices of surviving R robots
        
        for i in idx_by_pos:
            if directions[i] == 'R':
                stack.append(i)
            else:
                # L robot: resolve collisions with R robots to the left
                while stack and health[i] > 0:
                    j = stack[-1]
                    
                    if health[j] > health[i]:
                        # R survives, L dies
                        health[j] -= 1
                        health[i] = 0
                    elif health[j] < health[i]:
                        # L survives this collision, R dies
                        health[i] -= 1
                        health[j] = 0
                        stack.pop()
                    else:
                        # Both die
                        health[i] = 0
                        health[j] = 0
                        stack.pop()
                        break
        
        # Return survivors in original order
        return [health[i] for i in range(n) if health[i] > 0]