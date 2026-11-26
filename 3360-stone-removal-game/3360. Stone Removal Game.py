class Solution:
    def canAliceWin(self, n: int) -> bool:
        for stone_removal in range(10, -1, -1):
            if n - stone_removal < 0:
                return stone_removal % 2 != 0
            
            n -= stone_removal
