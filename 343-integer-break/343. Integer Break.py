class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        threes = n // 3
        twos = n % 3

        if twos == 0:
            return 3 ** threes
        elif twos == 1:
            return 3 ** (threes-1) * 2 * 2
        else:
            return 3 ** threes * 2

