class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMost = [0] * n
        leftMost[0] = height[0]
        for i in range(1,n):
            leftMost[i] = max(leftMost[i-1], height[i])
        leftMost = [0] + leftMost
        rightMost = [0] * n
        rightMost[-1] = height[-1]
        for i in range(len(height) -2, -1, -1):
            rightMost[i] = max(rightMost[i+1], height[i])
        rightMost = rightMost + [0]

        res = 0
        for i in range(len(height)):
            res += max(min(leftMost[i], rightMost[i]) - height[i], 0)
            print(i, res)
        return res