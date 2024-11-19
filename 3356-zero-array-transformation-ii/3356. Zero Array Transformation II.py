class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def compute(n):
            prefix = [0] * (len(nums) + 1)
            for l, r, v in queries[:n]:
                prefix[l] += v
                prefix[r + 1] -= v
            prefix = list(accumulate(prefix))
            return all(nums[i] <= prefix[i] for i in range(len(nums)))
        
        l, r = 0, len(queries)
        res = -1
        while l <= r:
            mid = l + (r-l) // 2
            if compute(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
