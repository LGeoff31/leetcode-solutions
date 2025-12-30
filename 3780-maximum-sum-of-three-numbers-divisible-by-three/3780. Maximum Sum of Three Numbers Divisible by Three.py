class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for n in nums:
            dic[n%3].append(n)
        for key in dic:
            dic[key] = sorted(dic[key])
        res = 0
        # contains 0
        if len(dic[0]) >= 3:
            res = max(res, dic[0][-1] + dic[0][-2] + dic[0][-3])
        if dic[0] and dic[1] and dic[2]:
            res = max(res, dic[0][-1] + dic[1][-1] + dic[2][-1])
        
        # contains 1
        if len(dic[1]) >= 3:
            res = max(res, dic[1][-1] + dic[1][-2] + dic[1][-3])
        
        # contains 2
        if len(dic[2]) >= 3:
            res = max(res, dic[2][-1] + dic[2][-2] + dic[2][-3])
        
        return res