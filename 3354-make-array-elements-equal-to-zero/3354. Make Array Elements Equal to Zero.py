class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
       
        for i in range(len(nums)):
            if nums[i] == 0:
                if abs(sum(nums[:i]) - sum(nums[i:])) == 1:
                    res += 1
                elif abs(sum(nums[:i]) - sum(nums[i:])) == 0:
                    res += 2
        return res