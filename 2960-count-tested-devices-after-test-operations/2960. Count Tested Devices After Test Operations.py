class Solution:
    def countTestedDevices(self, lst: List[int]) -> int:
        res = 0
        for i in range(len(lst)):
            if lst[i] > 0:
                res+=1
                for j in range(i+1, len(lst)):
                    lst[j] = max(0, lst[j]-1)
        return res
        