class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            n, r = n // 3, n % 3
            if r == 2:
                return False
        return True