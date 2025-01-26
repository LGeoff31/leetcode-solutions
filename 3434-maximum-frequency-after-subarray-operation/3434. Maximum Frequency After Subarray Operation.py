class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count = nums.count(k)
        res = 0

        for i in range(1, 51):
            if i == k: continue
            ans = 0
            curr = 0

            for num in nums:
                if num == i: curr += 1
                elif num == k: curr -= 1
                curr = max(curr, 0)
                ans = max(curr ,ans)
            res = max(res, ans)


        return res + count