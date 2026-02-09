class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        res = 0
        def isDominant(idx):
            total_sum = 0
            for i in range(idx + 1, len(nums)):
                total_sum += nums[i]
            if len(nums) - (idx + 1) != 0:
                return nums[idx] > total_sum / (len(nums) - (idx+1))
            return False
        cnt = 0
        for i in range(len(nums)):
            cnt += isDominant(i)
        return cnt