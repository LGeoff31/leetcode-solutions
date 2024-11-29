class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        lst = sorted([(a-b, a,b) for a,b in zip(reward1, reward2)], reverse=True)
        res = 0
        for i in range(k):
            res += lst[i][1]
        for i in range(k, len(reward1)):
            res += lst[i][2]
        return res
