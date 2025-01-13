class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        free = 0
        res = [0] * len(rains)
        free = SortedList()
        dic = {}
        for i in range(len(rains)):
            if rains[i] > 0:
                # Filling in the lake
                if rains[i] in dic and dic[rains[i]][0] == -1 and len(free) == 0:
                    return []
                elif rains[i] in dic and dic[rains[i]][0] == -1:
                    idx = bisect_left(free, dic[rains[i]][1])
                    if idx == len(free): return []
                    a = free[idx]
                    free.remove(a)
                    # idx = free.popleft()
                    # if idx < dic[rains[i]][1]:
                    #     return []
                    res[a] = rains[i]
                    res[i] = -1
                    dic[rains[i]] = [-1, i]
                else:
                    dic[rains[i]] = [-1, i]
                    res[i] = -1
            else:
                free.add(i)
            # print(res)
        for i in range(len(res)):
            if res[i] == 0:
                res[i] = 1
        return res
            