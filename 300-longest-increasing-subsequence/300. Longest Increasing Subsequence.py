class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                idx = bisect_left(stack, nums[i])
                stack[idx] = nums[i]
        return len(stack)