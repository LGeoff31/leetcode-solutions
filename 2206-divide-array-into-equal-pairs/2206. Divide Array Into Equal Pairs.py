class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        for key in dic:
            if dic[key] % 2:
                return False
        return True