class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:   
        dic = defaultdict(list)
        length = len(nums)
        for i, n in enumerate(nums):
            dic[n].append(i)
        res = []
        for q in queries:
            val = nums[q]
            indicies = dic[val]
            if len(indicies) <= 1:
                res.append(-1)
            else:
                idx = bisect_left(indicies, q)
                a = 1e9
                if idx >= len(indicies): 
                    res.append(-1)
                    continue

                a = min(a, abs(indicies[idx] - indicies[(idx-1)%len(indicies)]), length - abs(indicies[idx] - indicies[(idx-1)%len(indicies)]))
                a = min(a, abs(indicies[(idx+1) % len(indicies)] - indicies[idx]), length - abs(indicies[(idx+1) % len(indicies)] - indicies[idx]))
                res.append(a)

        return res
