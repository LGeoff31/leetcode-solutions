class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return list(set([n for n in nums if Counter(nums)[n] == 2]))