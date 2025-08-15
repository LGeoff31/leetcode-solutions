class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        # 2 ** 31 = 4 ** 16
        for i in range(17):
            if 4 ** i == n:
                return True
        return False