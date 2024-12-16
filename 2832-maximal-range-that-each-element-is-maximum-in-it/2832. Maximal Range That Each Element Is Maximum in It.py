class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        stack = [] # (idx, val) in decreasing order
        n = len(nums)
        ans = [0] * n
        nums.append(1e9)
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                idx, val = stack.pop()
                left = -1 if not stack else stack[-1][0]
                ans[idx] = i - left - 1
            stack.append((i, num))
        return ans
                        