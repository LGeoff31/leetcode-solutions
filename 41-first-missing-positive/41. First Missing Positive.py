class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:     
        a = set(nums)
        for i in range(1, 2**31):
            if i not in a:
                return i
        