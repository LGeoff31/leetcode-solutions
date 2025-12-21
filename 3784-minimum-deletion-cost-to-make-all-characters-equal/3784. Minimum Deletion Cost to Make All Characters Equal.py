class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(s)):
            letter, c = s[i], cost[i]
            dic[letter] += c
        
        total = sum(dic.values())
        return total - max(dic.values())