class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0


        for i in range(len(nums)):
            size, found = 0, 0
            for j in range(i, len(nums)):
                found += nums[j] == target
                size += 1
                res += found > size // 2

        return res