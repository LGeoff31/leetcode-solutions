class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triple = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if triple not in seen:
                            res.append(list(triple))
                            seen.add(triple)
        return res
