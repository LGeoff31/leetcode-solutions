class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        leftSum = sum(nums[:n//2])
        rightSum = sum(nums[n//2:])
        queue = deque(nums)

        for i in range(len(nums)):
            if leftSum > rightSum:
                res += 1
            leftSum -= queue[0]
            rightSum += queue[0]

            leftSum += queue[n//2]
            rightSum -= queue[n//2]
            
            queue.append(queue.popleft())
            
        return res