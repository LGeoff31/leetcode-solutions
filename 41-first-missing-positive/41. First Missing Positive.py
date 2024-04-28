class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #time complexity O(n)
        #space complexity O(n)
        a = set(nums)
        for i in range(1, max(nums)+2):
            if i not in a:
                return i
        return 1

        