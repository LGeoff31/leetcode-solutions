class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dic = Counter(s)
        numberOdds = 0
        for key in dic:
            if dic[key]%2==1: numberOdds+=1
        return True if numberOdds <= k and len(s) >=k else False

        