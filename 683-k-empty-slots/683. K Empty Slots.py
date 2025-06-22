class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        lst = SortedList()
        for i, pos in enumerate(bulbs):
            if len(lst) < 1:
                lst.add(pos)
            else:
                idx = bisect_left(lst, pos)
                if idx == 0:
                    if abs(lst[0]-pos) == k+1:
                        return (i+1)
                elif idx == len(lst):
                    if abs(lst[-1] - pos) == k+1:
                        return (i+1)
                else:
                    if abs(pos - lst[idx]) == k+1 or abs(pos - lst[idx - 1]) == k+1:
                        return (i+1)
                lst.add(pos)
                # print(lst, idx, pos)
        
        return -1

