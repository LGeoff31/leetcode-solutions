class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for key in dic:
            if dic[key] == 1: return key
        
        