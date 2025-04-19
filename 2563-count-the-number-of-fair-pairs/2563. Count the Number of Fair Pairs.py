class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0

        def bs(l, r, element):
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] >= element:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        for i in range(len(nums)): 
            low = bs(i+1, len(nums) - 1, lower - nums[i])
            high = bs(i+1, len(nums)-1, upper - nums[i] + 1)
            res += high - low
        return res