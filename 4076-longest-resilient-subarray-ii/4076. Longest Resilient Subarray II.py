class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        nums = [n % k for n in nums]
        res = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                curr += 1
                if nums[i] > 0 and (nums[i] * (curr - 1)) % k == 0:
                    res = max(res, curr)
            else:
                curr = 1
        print(res)
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and nums[i-1] == 0:
                curr += 1
            else:
                curr = 1
            res = max(res, curr)
        return res