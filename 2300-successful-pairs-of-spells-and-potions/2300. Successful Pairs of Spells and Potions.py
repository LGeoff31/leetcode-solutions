class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        dic = {}

        potions.sort()

        lst = [0] * len(spells)
        
        for i in range(len(spells)):
            count=0
            l, r = 0, len(potions) -1
            while l <= r:
                mid = (l+r)//2
                if (potions[mid] * spells[i] >= success and mid == 0 ) or (potions[mid] * spells[i] >= success and potions[mid-1] * spells[i] < success):
                    count = len(potions) - mid
                    break
                elif potions[mid] * spells[i] >= success:
                    r = mid - 1
                else:
                    l = mid + 1

            lst[i] = count

        return lst
        