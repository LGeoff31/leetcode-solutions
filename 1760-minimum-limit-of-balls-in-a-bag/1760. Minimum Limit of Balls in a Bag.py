class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        l, r = 1, max(nums)
        def valid(mid):
            if mid == 0: return True
            res = 0
            for num in nums:
                res += ceil(num/mid)
            return res <= maxOperations + n
        res = 1e9
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if valid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return int(res)