class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        dic = defaultdict(int)
        for b in bulbs:
            dic[b] += 1
        res = []
        for key in dic:
            if dic[key] % 2 == 1:
                res.append(key)
        res.sort()
        return res