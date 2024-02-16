from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = Counter(arr)
        lst = []
        for key in dic:
            lst.append(dic[key])
        lst.sort()

        count = len(set(arr))
        for num in lst:
            if k - num < 0:
                return count
            else:
                k -= num
                count -= 1
        return count