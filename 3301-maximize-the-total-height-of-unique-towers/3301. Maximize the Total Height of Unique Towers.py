class Solution:
    def maximumTotalSum(self, lst: List[int]) -> int:
        lst.sort(reverse=True)
        max_reachable = max(lst)
        i = 0
        res = 0
        while max_reachable != 0:
            if lst[i] >= max_reachable:
                res += max_reachable
                max_reachable -= 1
            else:
                res += lst[i]
                max_reachable = lst[i] - 1
            i += 1
            if i == len(lst): 
                return res
        return -1