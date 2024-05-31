class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        res = []
        for key in a:
            if a[key] == 1:
                res.append(key)
        return res