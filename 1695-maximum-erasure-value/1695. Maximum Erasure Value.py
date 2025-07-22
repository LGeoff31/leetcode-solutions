class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        l = 0
        dic = defaultdict(int)
        for r in range(len(nums)):
            dic[nums[r]] += 1
            curr += nums[r]
            while dic[nums[r]] >= 2:
                curr -= nums[l]
                dic[nums[l]] -= 1
                l += 1
            # print(dic, curr)
            res = max(res, curr)

        return res
