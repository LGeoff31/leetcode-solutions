class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        if k == 0: return len(set(nums))
        res = 0
        l = 0
        count = 0
        for r in range(len(nums)):
            dic[nums[r]] += 1
            count += dic[nums[r]] == 2
            while l < len(nums) and count > k:
                dic[nums[l]] -= 1
                if dic[nums[l]] == 1:
                    count -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1
            res = max(res, r-l+1)

        return res