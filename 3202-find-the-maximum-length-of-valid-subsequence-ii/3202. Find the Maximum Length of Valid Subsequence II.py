from collections import defaultdict
from functools import cache
from bisect import bisect_left

class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Reduce nums mod k
        for i in range(n):
            nums[i] %= k
        
        # Step 2: Group indices by mod value
        dic = defaultdict(list)
        for i, val in enumerate(nums):
            dic[val].append(i)

        # Step 3: Try all pair (a + b) % k values
        pair_sums = set()
        for i in range(n):
            for j in range(i + 1, n):
                pair_sums.add((nums[i] + nums[j]) % k)

        @cache
        def dfs(i: int, target: int, s: int) -> int:
            if target not in dic:
                return 1  # Can't continue the chain

            idx_list = dic[target]
            pos = bisect_left(idx_list, i)  # Find next valid index >= i

            max_len = 1
            while pos < len(idx_list):
                j = idx_list[pos]
                next_target = (s - nums[j]) % k
                max_len = max(max_len, 1 + dfs(j + 1, next_target, s))
                pos += 1

            return max_len

        res = 0
        for s in pair_sums:
            for i in range(n):
                target = (s - nums[i]) % k
                res = max(res, dfs(i + 1, target, s) + 1)  # +1 for nums[i] itself

        return res-1
