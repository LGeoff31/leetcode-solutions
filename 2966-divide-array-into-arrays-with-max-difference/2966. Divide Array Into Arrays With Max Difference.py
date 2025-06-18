class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # sort
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            group = [nums[i], nums[i+1], nums[i+2]]
            if max(group) - min(group) > k:
                return []
            res.append(group)
        return res