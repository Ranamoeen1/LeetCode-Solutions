class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        # Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Get coordinates for rectangle i
                a1, b1 = bottomLeft[i]
                c1, d1 = topRight[i]
                
                # Get coordinates for rectangle j
                a2, b2 = bottomLeft[j]
                c2, d2 = topRight[j]
                
                # Check if rectangles intersect
                # x-intervals must overlap
                x_left = max(a1, a2)
                x_right = min(c1, c2)
                
                # y-intervals must overlap
                y_bottom = max(b1, b2)
                y_top = min(d1, d2)
                
                # If there's valid intersection
                if x_left < x_right and y_bottom < y_top:
                    width = x_right - x_left
                    height = y_top - y_bottom
                    
                    # Maximum square side that fits is min(width, height)
                    side = min(width, height)
                    max_side = max(max_side, side)
        
        # Return area
        return max_side * max_side