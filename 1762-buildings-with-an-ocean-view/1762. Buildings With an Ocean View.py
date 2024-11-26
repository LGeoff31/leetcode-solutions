class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prefix = [0] * len(heights)
        prefix[-1] = heights[-1]
        for i in range(len(prefix) - 2, -1, -1):
            prefix[i] = max(heights[i], prefix[i+1])
        res = []
        for i in range(len(heights)):
            if i == len(heights) - 1: 
                res.append(i)
                break 
            if heights[i] > prefix[i+1]:
                res.append(i)
        return res
            

