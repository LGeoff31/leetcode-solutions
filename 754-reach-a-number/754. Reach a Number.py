class Solution:
    def reachNumber(self, target: int) -> int:
        # 5: 1+2+3+4+5 = 15, want subtract 10, 2(1+4)
        def valid(mid):
            currSum = mid * (mid + 1) // 2
            if currSum < abs(target):
                return False
            diff = currSum - target
            if diff % 2 == 1:
                return False
            if diff > 2*currSum:
                return False
            return True
        for i in range(1, 10 ** 5):
            if valid(i):
                return i
        # l, r = 0, 10 ** 5
        # moves = 1e9
        # while l <= r:
        #     mid = (l + r) // 2
        #     print('trying', mid)
        #     if valid(mid):
        #         print('got', mid)
        #         moves = min(moves, mid)
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        return -1
