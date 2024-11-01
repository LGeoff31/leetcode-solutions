class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        @cache
        def dfs(i): #O(n)
            if i >= len(energy):
                return 0
            
            return energy[i] + dfs(i+k)
        res = min(energy)
        for i in range(len(energy)): #O(n)
            res = max(res, dfs(i))
        return res