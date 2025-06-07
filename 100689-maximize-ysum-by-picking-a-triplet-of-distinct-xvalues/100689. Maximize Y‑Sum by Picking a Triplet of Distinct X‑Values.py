class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        if len(set(x)) <= 2:
            return -1
        dic=defaultdict(int)
        for i in range(len(x)):
            dic[x[i]] = max(dic[x[i]], y[i])
        lst = sorted([(dic[key], key) for key in dic], reverse=True)
        res = 0
        for i in range(3):
            res += lst[i][0]
        return res