class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        queue = deque(nums)
        n = len(nums)
        totalSum = sum(nums)
        res = 0
        # Initialize
        for i in range(len(nums)):
            res += i * nums[i]
        prev = res
        for i in range(n-1):
            rightElement = queue.pop()
            queue.appendleft(rightElement)
            res = max(res, prev + totalSum - n * rightElement)
            prev = prev + totalSum - n * rightElement
            # print(prev + totalSum - n * rightElement, queue)
        return res
