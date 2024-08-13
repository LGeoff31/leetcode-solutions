class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, arr):
            if sum(arr) == target:
                res.append(arr.copy())
                return
            if sum(arr) > target or i >= len(candidates):
                return
           
            arr.append(candidates[i])
            dfs(i+1, arr)
            arr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, arr)
            
        dfs(0, [])
        return res
