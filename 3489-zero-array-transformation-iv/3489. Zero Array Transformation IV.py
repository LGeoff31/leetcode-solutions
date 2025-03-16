class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0: return 0
        @cache
        def dfs(val, k, i):
            if val == 0:
                return True 
            if k < 0 or val < 0:
                return False
            if k >= len(queries):
                return False
            
            # Take
            res = False
            if queries[k][0] <= i <= queries[k][1]:
                res = res or dfs(val - queries[k][2], k-1, i)
            res = res or dfs(val, k-1, i)
            return res
        def valid(mid):
            for i in range(len(nums)):
                if not dfs(nums[i], mid, i): # 1000, 1000, 10
                    return False
            return True
        l, r = 0, len(queries)
        res = 1e9
        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res + 1 if res != 1e9 else -1