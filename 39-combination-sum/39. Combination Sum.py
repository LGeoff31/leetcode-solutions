class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(num, lst):
            #base cases
            if num > target:
                return
            if num == target:
                lst.sort()
                if lst not in res:
                    res.append(lst)
            #recursion
            for num in candidates:
                dfs(sum(lst)+num, lst + [num])

        for num in candidates:
            dfs(num, [num])
        return res

        