from sortedcontainers import SortedList
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        if max(maximumHeight) < len(maximumHeight): return -1
        maximumHeight.sort()
        res = 0
        visited = set()
        a = SortedList()
        # print(maximumHeight)
        for i in range(len(maximumHeight) -1, -1, -1):
            if maximumHeight[i] not in visited:
                res += maximumHeight[i]
                visited.add(maximumHeight[i])
                a.add(maximumHeight[i])
            else:
                num = maximumHeight[i]
                # while num in visited:
                #     num -= 1
                num = a[0] - 1
                if num == 0: return -1
                res += num
                visited.add(num)
                a.add(num)
            # print(a)
        return res
        