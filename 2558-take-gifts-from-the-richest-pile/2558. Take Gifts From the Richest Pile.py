from sortedcontainers import SortedList
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        lst = SortedList(gifts)

        for i in range(k):
            num = lst[-1]
            lst.pop()
            lst.add(floor(sqrt(num)))

        return sum(lst)