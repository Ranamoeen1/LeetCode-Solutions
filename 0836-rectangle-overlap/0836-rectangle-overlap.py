class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Unpack rectangle coordinates
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # Check if intervals overlap on both x-axis and y-axis
        x_overlap = max(x1, x3) < min(x2, x4)
        y_overlap = max(y1, y3) < min(y2, y4)
        
        return x_overlap and y_overlap