class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        def valid(mid):
            return sum(ceil(num / mid) for num in nums) <= threshold
        res = 1e9
        while l <= r:
            mid = l + (r-l) // 2
            print('tring mid', mid, valid(mid))
            if valid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res