class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = {}
        l, r = 0, 0
        res = 0
        a = 0
        while r < len(nums):
            if nums[r] in dic:
                dic[nums[r]] += 1
                res+=1 #7
                if dic[nums[r]] > k:
                    while dic[nums[r]] > k and l < len(nums):
                        dic[nums[l]] -= 1
                        l+=1
                        res-=1
            else:
                dic[nums[r]] = 1
                res+=1
            r+=1
            a = max(a, res)
        return a
                    
                    
        