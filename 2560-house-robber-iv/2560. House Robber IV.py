class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Robber steal from at least k houses
        # Want minimize house with most money
        # No adjacent houses

        l, r = min(nums), max(nums)
        res = 1e9

        def valid(val):
            idx = 0
            count = 0
            while idx < len(nums):
                if nums[idx] <= val:
                    count += 1
                    idx += 2
                else:
                    idx += 1
            return count >= k
        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return int(res)