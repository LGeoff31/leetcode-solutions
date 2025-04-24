class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        l, r = 0, 0
        res = 0
        unique = len(set(nums))
        while r < len(nums):
            while r < len(nums) and len(dic) != unique:
                dic[nums[r]] += 1
                r += 1
            if len(dic) == unique:
                res += len(nums) - r + 1
            print(res, dic)
            dic[nums[l]] -= 1
            if dic[nums[l]] == 0:
                del dic[nums[l]]
            l += 1
        while l < len(nums):
            if len(dic) == unique:
                res += 1
            dic[nums[l]] -= 1
            if dic[nums[l]] == 0:
                del dic[nums[l]]
            l += 1
            # r += 1
        return res