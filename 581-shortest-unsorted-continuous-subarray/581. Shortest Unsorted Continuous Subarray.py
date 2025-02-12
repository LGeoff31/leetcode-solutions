class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = 1e9, -1e9

        # Find start
        stack = [] # (val, idx)
        idx = 0
        while idx < len(nums):
            while stack and nums[idx] < stack[-1][0]:
                val, i = stack.pop()
                start = min(start, i)
            stack.append((nums[idx], idx))
            idx += 1
        
        # Find end
        stack = []
        idx = len(nums) - 1
        while idx >= 0:
            while stack and nums[idx] > stack[-1][0]:
                val, i = stack.pop()
                end = max(end, i)
            stack.append((nums[idx], idx))
            idx -= 1
        print(start)
        print(end)

        return end-start+1 if start < 10000 else 0
