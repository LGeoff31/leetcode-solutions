class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        res = []
        for key in a:
            if a[key] == 2:
                res.append(key)
        return res
        