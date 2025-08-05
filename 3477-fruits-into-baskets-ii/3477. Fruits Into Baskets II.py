class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for f in fruits:
            for i in range(len(baskets)):
                if baskets[i] > 0 and f <= abs(baskets[i]):
                    baskets[i] = -baskets[i]
                    break
            else:
                res += 1
        return res