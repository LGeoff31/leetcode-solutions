class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        dic = {}
        for i in range(k):
            curr += nums[i]
            dic[nums[i]] = 1 + dic.get(nums[i], 0)

        if len(dic) == k:
            res = curr
        # Start the window slider
        l, r = 0, k
        while r < len(nums):
            dic[nums[l]] -= 1
            if dic[nums[l]] == 0:
                del dic[nums[l]]
            curr -= nums[l]

            curr += nums[r]
            dic[nums[r]] = 1 + dic.get(nums[r], 0)
            if len(dic) == k:
                # print(dic, l, r)
                res = max(res, curr)
            
            r += 1
            l += 1
        return res