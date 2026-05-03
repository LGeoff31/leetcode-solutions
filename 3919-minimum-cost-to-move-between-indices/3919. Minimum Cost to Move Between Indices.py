class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        closest = [0] * n

        for i in range(len(nums)):
            if i == 0:
                closest[i] = 1
            elif i == n - 1:
                closest[i] = n-2
            else:
                left, right = abs(nums[i] - nums[i-1]), abs(nums[i+1] - nums[i])
                if left <= right:
                    closest[i] = i-1
                else:
                    closest[i] = i+1
            
        forward = [0] * n
        backward = [0] * n

        for i in range(len(nums) - 1):
            if closest[i] == i+1:
                forward[i + 1] = forward[i] + 1
            else:
                forward[i + 1] = forward[i] + (nums[i+1] - nums[i])

        for i in range(n - 1, 0, -1):
            if closest[i] == i - 1:
                backward[i - 1] = backward[i] + 1
            else:
                backward[i-1] = backward[i] + (nums[i] - nums[i-1])

        res = []
        for l,r in queries:
            if l < r:
                res.append(forward[r] - forward[l])
            else:
                res.append(backward[r] - backward[l])
        return res