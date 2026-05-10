class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        adj = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    adj[i].append(j)
        @cache
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            
            res = -1e9
            for nei in adj[i]:
                res = max(res, 1 + dfs(nei))
            return res
        
        return dfs(0) if dfs(0) > 0 else -1