class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            for c in str(n):
                res.append(int(c))
        return res