class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        def is_stable(i):
            return max(nums[: i + 1]) - min(nums[i : ]) <= k

        for i in range(len(nums)):
            if is_stable(i):
                return i
        
        return -1