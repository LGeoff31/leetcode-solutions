class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        minX, maxX = 1e9, -1e9
        minY, maxY = 1e9, -1e9

        rows, cols = len(image), len(image[0])
        for r in range(rows):
            for c in range(cols):
                if image[r][c] == "1":
                    minX = min(minX, c)
                    maxX = max(maxX, c)
                    minY = min(minY, r)
                    maxY = max(maxY, r)
        return (maxX - minX + 1) * (maxY - minY + 1)