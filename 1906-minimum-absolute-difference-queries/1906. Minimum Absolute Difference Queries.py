class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i, n in enumerate(nums):
            dic[n].append(i)
        res = []
        for s, e in queries:
            existing_nums = []
            for n in dic:
                if bisect_left(dic[n], s) != bisect_right(dic[n], e):
                    existing_nums.append(n)
            if len(existing_nums) >= 2:
                min_diff = 1e9
                existing_nums.sort()
                for i in range(1, len(existing_nums)):
                    min_diff = min(min_diff, existing_nums[i] - existing_nums[i-1])
                res.append(min_diff)
            else:
                res.append(-1)
        return res
