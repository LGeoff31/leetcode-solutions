class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = 1e9
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        res = min(res, j-i + k-i + k-j)
        return res if res != 1e9 else -1