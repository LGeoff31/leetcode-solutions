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
            leftSum -= nums[i]
            rightSum += nums[i]

            leftSum += nums[(i + n//2) % n]
            rightSum -= nums[(i + n//2) % n]
            
            queue.append(queue.popleft())
            
        return res