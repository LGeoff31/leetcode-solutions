class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        left = [nums[0]]
        a = nums.copy()
        right = a[::-1]
        res = 1e9
        def increasing(nums):
            stack = []
            for i in range(len(nums)):
                idx = bisect_left(stack, nums[i])
                if idx == len(stack):
                    stack.append(nums[i])
                else:
                    stack[idx] = nums[i]
            return len(stack)

        for i in range(1, len(nums) - 1):
            # Place peak at index i
            left.append(nums[i])
            right.pop()
            a,b = increasing(left), increasing(right)
            if a > 1 and b > 1:
                print(a,b)
                res = min(res, len(nums) - a - b + 1)

        return res