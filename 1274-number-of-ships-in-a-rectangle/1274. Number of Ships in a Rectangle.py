# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        res = 0

        def dfs(bottomLeft, topRight):
            # Base case: if the rectangle is invalid
            if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
                return 0
            
            # Base case: if the rectangle has no ships
            if not sea.hasShips(topRight, bottomLeft):
                return 0
            
            # Base case: if the rectangle is a single point
            if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
                return 1

            # Calculate the midpoints to split the rectangle
            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2

            # Recurse on the four quadrants
            return (
                dfs(bottomLeft, Point(midX, midY)) +
                dfs(Point(midX + 1, bottomLeft.y), Point(topRight.x, midY)) +
                dfs(Point(bottomLeft.x, midY + 1), Point(midX, topRight.y)) +
                dfs(Point(midX + 1, midY + 1), topRight)
            )
        
        return dfs(bottomLeft, topRight)
