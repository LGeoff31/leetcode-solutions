class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        res = [0] * len(heroes)
        lst = [[a,b] for a,b in zip(monsters, coins)]
        lst.sort()
        monsters = [a for a,b in lst]
        coins = [b for a,b in lst]
        prefix = list(accumulate(coins))
        
        for i in range(len(heroes)):
            idx = bisect.bisect_right(monsters, heroes[i])
            if idx > 0:
                res[i] = prefix[bisect.bisect_right(monsters, heroes[i]) - 1]
        return res