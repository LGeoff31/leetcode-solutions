class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        # Binary search??
        # [1,2,9,10]
        # If we pick 1, ans = 1 + 8 + 9 = 18
        # If we pick 2, ans = 1 + 7 + 8 = 16
        # If we pick 9, ans = 8 + 7 + 1 = 16
        # If we pick 10, ans = 9 + 8 + 1 = 18

        # There is a weighted shift between elements
        # Hence, binary search if effective
        l, r = 0, len(nums) - 1
        def calc(num):
            res = 0
            for n in nums:
                res += abs(num - n)
            return res
        while l <= r:
            mid = (l + r) // 2
            if mid == 0: return calc(nums[mid])
            if mid == len(nums) - 1: return calc(nums[mid])

            target = nums[mid]
            if calc(nums[mid-1]) >= calc(nums[mid]) and calc(nums[mid]) <= calc(nums[mid+1]):
                return calc(nums[mid])
            elif calc(nums[mid-1]) < calc(nums[mid]):
                r = mid - 1
            else:
                l = mid + 1
        return -1
