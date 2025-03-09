class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = -1
                    break
        res = 0
        for i in range(len(baskets)):
            res += baskets[i] != -1
        return res