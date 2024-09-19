class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        print(height)
        print(leftMax)
        print(rightMax)
        for i in range(1, n-1):
            # leftMax = rightMax = 0
            # for l in range(i, -1, -1):
            #     leftMax = max(leftMax, height[l])
            # for r in range(i, n):
            #     rightMax = max(rightMax, height[r])

            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
