class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #3 pointer technique
        dic = {}
        far, near, r = 0, 0, 0
        res = 0
        while r < len(nums):
            dic[nums[r]] = 1 + dic.get(nums[r], 0)
            if len(dic) == k:
                while dic[nums[near]] > 1:
                    dic[nums[near]]-=1
                    near+=1
                    if dic[nums[near]] == 0:
                        del dic[nums[near]]
                res+=near-far+1
            elif len(dic) > k:
                while len(dic) > k:
                    dic[nums[near]]-=1
                    if dic[nums[near]] == 0:
                        del dic[nums[near]]
                    near+=1
                    far = near
                dic[nums[r]]-=1
                r-=1
            else:
                pass
            r+=1
            # print(dic, res)
        return res
                
        