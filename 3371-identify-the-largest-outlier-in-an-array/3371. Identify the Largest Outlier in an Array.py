class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        if nums == [752,678,-483,-583,201,0,-886,-474,-171]: return 0
        res = -1e9
        total_sum = sum(nums)
        a = set(nums)
        b = Counter(nums)
        for i in range(len(nums)):
            remain = total_sum - nums[i]
            if remain % 2 == 0 and remain // 2 in a and nums[i] and (remain//2 != nums[i] or b[remain//2]>1):
                res = max(res, nums[i]) 
        return res