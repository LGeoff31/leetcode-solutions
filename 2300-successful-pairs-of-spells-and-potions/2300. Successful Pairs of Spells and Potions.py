class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for s in spells:
            res.append(len(potions) - bisect_left(potions, success/s))
        return res