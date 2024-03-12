class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        a = str(nums[0])
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            else:
                if a != str(nums[i-1]): a += "->" + str(nums[i-1])
                res.append(a)
                a = str(nums[i])
        if a!=str(nums[i]): a += "->" + str(nums[i])
        res.append(a)
        return res
        