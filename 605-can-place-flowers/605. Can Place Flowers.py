class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if i == 0:
                if len(flowerbed) == 1:
                    if n == 0: return True
                    if flowerbed[0] == 0 and n == 1: return True
                    return False
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] != 1 and flowerbed[i-1] != 1:
                    count += 1
            else:
                if flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    count += 1
        return count >= n   
        