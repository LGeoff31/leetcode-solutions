class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        print(nums)

        for i in range(len(nums)):
            s,e = lower - nums[i], upper - nums[i]
            s_idx, e_idx = bisect_left(nums, s), bisect_right(nums, e)
            # if e_idx <= i: continue
            res += max(bisect_right(nums, e) - max(i,s_idx) - (s <= nums[i] <= e),0)
            print(res)
        return res