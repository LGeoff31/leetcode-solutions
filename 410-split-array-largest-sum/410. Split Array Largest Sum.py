class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = list(accumulate(nums))
        @cache
        def dfs(idx, subarrays):
            if subarrays == 1:
                return prefix[-1] - (prefix[idx-1] if idx-1 >= 0 else 0)
            
            res = 1e9
            for i in range(idx, n - subarrays + 1):
                res = min(res, max(prefix[i] - (prefix[idx-1] if idx-1 >= 0 else 0), dfs(i+1, subarrays - 1)))
            return res
        return dfs(0, k)
