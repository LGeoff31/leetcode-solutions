class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        n = len(nums)
        res = n * (n+1) // 2
        curr = 0
        length = 0
        ans = 0
        while r < n:
            # Make window invalid
            while r < n and curr < k:
                if length == 0:
                    curr += nums[r]
                    length += 1
                else:
                    curr = (curr / length + nums[r]) * (length + 1)
                    length += 1
                r += 1
            r -= 1
            if curr >= k:
                ans += len(nums) - r
            # print('a', l, r, curr, length)
            curr = (curr-length*nums[l]) * ((length-1) / length)
            length -= 1
            l += 1
            # print('b', l, r, curr, length)
            # print('c', ans)
            r += 1
        while l < n and curr >= k:
            curr = (curr-length*nums[l]) * ((length-1) / length)
            length -= 1
            l += 1
            ans += 1

        print(ans)
        return res - ans
