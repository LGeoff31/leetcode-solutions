class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i+1 < len(flowerbed) and flowerbed[i+1] == 1:
                    i += 3
                else:
                    n -= 1
                    i += 2
            else:
                i += 2
        
        return n <= 0
