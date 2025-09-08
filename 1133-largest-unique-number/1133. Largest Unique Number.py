class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        res = 0
        dic = Counter(nums)
        for key in dic:
            if dic[key] == 1:
                res = max(res, key)
        return res if res != 0 else -1