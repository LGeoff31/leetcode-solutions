class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        dic = Counter(nums)

        for key in dic:
            if dic[key] == 2:
                res ^= key
        return res        