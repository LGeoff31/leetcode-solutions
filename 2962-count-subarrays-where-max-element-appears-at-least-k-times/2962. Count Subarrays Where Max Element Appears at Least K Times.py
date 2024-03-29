class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        dic = {}
        l,r = 0, 0
        maxNum = max(nums)
        res = 0
        while l < len(nums):
            dic[nums[r]] = 1 + dic.get(nums[r], 0)
            if nums[r] == maxNum and dic[nums[r]] >= k:
                res+=len(nums)-r
                dic[nums[l]] -= 1
                l+=1
                dic[nums[r]] -= 1
            else:
                r+=1
                if r == len(nums): break
        return res