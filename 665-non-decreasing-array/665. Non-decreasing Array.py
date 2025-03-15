class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []

        for i in range(len(nums)):
            idx = bisect_right(stack, nums[i])
            if idx == len(stack):
                stack.append(nums[i])
            else:
                stack[idx] = nums[i]
        return n - len(stack) <= 1