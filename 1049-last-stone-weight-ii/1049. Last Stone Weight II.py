class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        res = 1e9 
        @cache
        def dfs(i, currSum): # O(n * 3000 * 2)
            nonlocal res

            if i == len(stones):
                if currSum >= 0:
                    res = min(res, currSum)
                return 
            
            dfs(i+1, currSum + stones[i])

            dfs(i+1, currSum - stones[i])
        
        dfs(0, 0)
        return res