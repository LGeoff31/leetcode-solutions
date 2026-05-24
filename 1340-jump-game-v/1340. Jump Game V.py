class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """
        precomptue max[i][j] = max b/w subarr[i:j]

        """
        @cache
        def dfs(i):       
            res = 0
            maxLeft = -1e9
            for delta in range(1,d+1):
                if i-delta >= 0:
                    maxLeft=max(maxLeft, arr[i-delta])
                    if maxLeft < arr[i]:
                        res = max(res, 1 + dfs(i-delta))
                    else:
                        break
            maxRight = -1e9
            for delta in range(1,d+1):            
                if i+delta < len(arr):
                    maxRight=max(maxRight, arr[i+delta])
                    if maxRight < arr[i]:
                        res = max(res, 1 + dfs(i+delta))
                    else:
                        break
            return res

        res = 0
        for i in range(len(arr)):
            res = max(res, dfs(i))
        return res + 1
                        
