class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the point on the rectangle closest to the circle's center
        nearestX = max(x1, min(xCenter, x2))
        nearestY = max(y1, min(yCenter, y2))
        
        # Calculate the distance between the circle's center and this closest point
        distX = xCenter - nearestX
        distY = yCenter - nearestY
        
        # Check if the squared distance is within the squared radius
        return (distX ** 2 + distY ** 2) <= (radius ** 2)