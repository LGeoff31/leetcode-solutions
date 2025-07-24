class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for mask in range(1 << n):
            cur = []
            for i in range(n):
                if mask & (1 << i):
                    cur.append(nums[i])
            res.append(cur)
        return res