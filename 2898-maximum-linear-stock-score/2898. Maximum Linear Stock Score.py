class Solution:
    def maxScore(self, prices: List[int]) -> int:
        group = []
        for i in range(len(prices)):
            group.append(prices[i] - i)
        res = 0
        dic = defaultdict(list)
        for i in range(len(group)):
            dic[group[i]].append(i)
        for key in dic:
            count = 0
            arr = dic[key]
            for idx in arr:
                count += prices[idx]
            res = max(res, count)

        print(group)
        return res