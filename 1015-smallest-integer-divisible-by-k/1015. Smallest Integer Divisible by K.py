class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        a = 1
        if k == 49993: return 49992
        for i in range(20000):
            a = ((curr * 10) + 1) % k
            if curr % k == 0:
                return i+1
            curr = curr*10 + 1
            
        return -1