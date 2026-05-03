class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        n = len(nums)
        v = []

        for i in range(n):
            if nums[i] <= i:
                v.append((i - nums[i], nums[i]))

        if not v:
            return 0

        v.sort()

        lis = []

        for d, val in v:
            idx = bisect_left(lis, val)

            if idx == len(lis):
                lis.append(val)
            else:
                lis[idx] = val

        return len(lis)