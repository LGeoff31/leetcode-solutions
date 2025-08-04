class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(fruits)):
            dic[fruits[r]] += 1

            while len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    del dic[fruits[l]]
                l += 1
            res = max(res, sum(dic[key] for key in dic))

        return res