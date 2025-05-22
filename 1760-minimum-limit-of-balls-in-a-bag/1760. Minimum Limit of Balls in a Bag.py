class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, 1e9
        res = 1e9
        def valid(val):
            if val == 0: return True
            # we want all the values of nums ot be <= val
            operations = 0
            for n in nums:
                if n > val:
                    operations += ceil(n/val)-1
            return operations <= maxOperations
        while l <= r:
            mid = (l + r) // 2
            print('trying mid', mid)
            if valid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return int(res)

        # 2 4 8 2
        # 4


        # 9 -> 4, 5

        #1000000000,1000000000,1000000000
        #1000000000
        #500000000