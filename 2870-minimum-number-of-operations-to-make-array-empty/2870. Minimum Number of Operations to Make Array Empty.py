class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        dic = Counter(nums)
        @cache
        def min_operations(n):
            if n <= 3:
                return 1
            return 1 + min_operations(n-3)

        for key in dic:
            if dic[key] == 1:
                return -1
            res += min_operations(dic[key])
        return res