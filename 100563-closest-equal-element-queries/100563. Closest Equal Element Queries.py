class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        dic = defaultdict(list)
        n = len(nums)
        a = Counter(nums)
        nums = nums + nums
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        for query in queries:
            ans = 1e9
            # First position
            val = nums[query]
            idx = dic[val]
            ans = min(ans, idx[bisect_right(idx, query)] - query, query + n - idx[bisect_left(idx, query + n) - 1])
            if idx[0] != query:
                ans = min(ans, query - idx[bisect_left(idx, query) - 1])
            res.append(ans if a[nums[query]] > 1 else -1)
        return res