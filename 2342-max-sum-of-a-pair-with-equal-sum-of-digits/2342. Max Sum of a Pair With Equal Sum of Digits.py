class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(SortedList)
        def sum(num):
            res = 0
            for n in str(num):
                res += int(n)
            return res
        for num in nums:
            dic[sum(num)].add(num)
        res = -1
        for key in dic:
            if len(dic[key]) >= 2:
                res = max(res, dic[key][-1] + dic[key][-2])
        return res