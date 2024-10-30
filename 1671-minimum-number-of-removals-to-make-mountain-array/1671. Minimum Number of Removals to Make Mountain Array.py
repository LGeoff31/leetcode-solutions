class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        a = []
        b = []
        def increasing(nums, option):
            stack = []
            for i in range(len(nums)):
                idx = bisect_left(stack, nums[i])
                if idx == len(stack):
                    stack.append(nums[i])
                else:
                    stack[idx] = nums[i]
                if option:
                    a.append(len(stack))
                else:
                    b.append(len(stack))
        increasing(nums, 1)
        increasing(nums[::-1], 0)
        res = 1e9
        for i in range(1, len(a) - 1):
            if a[i] > 1 and b[len(nums) - i - 1] > 1:
                res = min(res, len(nums) - (a[i] + b[len(nums) - i - 1]) + 1) 
                if res == 4: print(i)
        print(a)
        print(b)

        return res