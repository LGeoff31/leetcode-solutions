class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        res = 0
        n = len(nums)
        current = 0
        l, r = 0, 0
        while r < len(nums): 
            while r < len(nums) and current < k:
                dic[nums[r]] += 1
                current += dic[nums[r]] - 1
                r += 1
            print(res, l, r, current)
            if current >= k:
                res += n - r + 1
            dic[nums[l]] -= 1
            current -= dic[nums[l]]
            l += 1

        print(res, l, r, current)
        while l < len(nums):
            if current >= k:
                res += 1
            dic[nums[l]] -= 1
            current -= dic[nums[l]] 
            l += 1
        return res

