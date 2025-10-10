class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = -1e9
        @cache
        def dfs(idx):
            if idx >= len(energy):
                return 0
            return energy[idx] + dfs(idx + k)
        for i in range(len(energy)):
            res = max(res, dfs(i))
        return int(res)