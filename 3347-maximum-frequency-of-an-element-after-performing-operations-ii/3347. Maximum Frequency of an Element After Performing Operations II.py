from bisect import bisect_left, bisect_right

class Solution:
    def check(self, nums, n, t, m):
        nL = n
        tL = t
        l = bisect_left(nums, nL)
        h = bisect_right(nums, nL)
        ll = bisect_left(nums, nL - tL)
        hh = bisect_right(nums, nL + tL)
        res = (hh - h) + (l - ll)
        return min(m, res) + (h - l)

    def maxFrequency(self, nums, k, numOperations):
        m = numOperations
        nums.sort()
        ans = 1
        for i in range(len(nums) - 1):
            ans = max(ans, self.check(nums, nums[i], k, m))
            ans = max(ans, self.check(nums, nums[i] - k, k, m))
            ans = max(ans, self.check(nums, nums[i] + k, k, m))
        return ans