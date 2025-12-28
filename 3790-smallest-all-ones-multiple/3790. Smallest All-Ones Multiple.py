class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        res = 1
        cnt = 1
        while cnt < 100000:
            if res % k == 0:
                return cnt
            res = ((res * 10) + 1) % k
            cnt += 1
        return -1