class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curr = 0
        if 1 not in nums: return True
        idx = nums.index(1)
        for i in range(idx + 1, len(nums)):
            if nums[i] == 1:
                if curr < k:
                    return False
                curr = 0
            else:
                curr += 1
        return True
