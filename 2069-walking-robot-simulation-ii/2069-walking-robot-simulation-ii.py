class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0  # Position along perimeter (0-indexed)
        self.has_moved = False
        
    def step(self, num: int) -> None:
        if num > 0:
            self.has_moved = True
        perimeter = 2 * (self.w + self.h - 2)
        self.pos = (self.pos + num) % perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        w, h = self.w, self.h
        
        # Bottom edge (East): x from 0 to w-1, y=0
        if p < w:
            return [p, 0]
        
        # Right edge (North): x=w-1, y from 1 to h-1
        p -= w
        if p < h - 1:
            return [w - 1, 1 + p]
        
        # Top edge (West): x from w-2 down to 0, y=h-1
        p -= (h - 1)
        if p < w - 1:
            return [w - 2 - p, h - 1]
        
        # Left edge (South): x=0, y from h-2 down to 1
        p -= (w - 1)
        return [0, h - 2 - p]

    def getDir(self) -> str:
        # At origin without moving: East
        if self.pos == 0 and not self.has_moved:
            return "East"
        # At origin after moving: South (arrived from left edge going down)
        if self.pos == 0 and self.has_moved:
            return "South"
            
        p = self.pos
        w, h = self.w, self.h
        
        # Determine which edge we're on
        if p < w:
            return "East"
        p -= w
        if p < h - 1:
            return "North"
        p -= (h - 1)
        if p < w - 1:
            return "West"
        return "South"



# class Robot:

#     def __init__(self, width: int, height: int):
#         self.w = width
#         self.h = height
#         self.x = 0
#         self.y = 0
#         # 0: East, 1: North, 2: West, 3: South
#         self.dir = 0
#         self.dirs = ["East", "North", "West", "South"]
#         self.dx = [1, 0, -1, 0]
#         self.dy = [0, 1, 0, -1]
#         self.has_moved = False

#     def step(self, num: int) -> None:
#         perimeter = 2 * (self.w + self.h - 2)
#         remainder = num % perimeter
        
#         # If we completed full cycles (remainder is 0 but num > 0)
#         if remainder == 0 and num > 0:
#             self.has_moved = True
#             # Only at (0,0) we end up facing South after full cycle
#             if self.x == 0 and self.y == 0:
#                 self.dir = 3  # South
#             # At other positions, we return to same position with same direction
#             return
        
#         # Process remaining steps
#         while remainder > 0:
#             self.has_moved = True
#             nx = self.x + self.dx[self.dir]
#             ny = self.y + self.dy[self.dir]
            
#             # Check if next position is out of bounds
#             if nx < 0 or nx >= self.w or ny < 0 or ny >= self.h:
#                 # Turn counterclockwise (90 degrees)
#                 self.dir = (self.dir + 1) % 4
#             else:
#                 # Move to next position
#                 self.x, self.y = nx, ny
#                 remainder -= 1

#     def getPos(self) -> list[int]:
#         return [self.x, self.y]

#     def getDir(self) -> str:
#         # Special case: at origin and never moved
#         if self.x == 0 and self.y == 0 and not self.has_moved:
#             return "East"
#         return self.dirs[self.dir]