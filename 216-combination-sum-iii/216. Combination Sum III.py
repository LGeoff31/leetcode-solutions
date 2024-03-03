class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(target, lst):
            if sum(lst) == n and len(lst) == k and sorted(lst) not in res:
                res.append(lst) 
            elif sum(lst) < n and len(lst) < k:
                for i in range(1, 10):
                    newTarget = target - i
                    if i not in lst:
                        dfs(newTarget, lst + [i])
        dfs(n, [])

        return res
            # res.append([i] + pairArray(i, target))
        