class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idx = []
        for i in range(len(nums)):
            if nums[i] == x:
                idx.append(i)
        res = []
        for query in queries:
            if query > len(idx):
                res.append(-1)
            else:
                res.append(idx[query-1])
        return res
                

        