class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def calc(num):
            digits = [0, *map(int, str(num))]
            @cache
            def dfs(i, diff, digitlim):
                if i == len(digits):
                    return int(diff) == 0

                maxdigit = digits[i] if digitlim else 9
                possign = 2 * int(i % 2) - 1 # either -1 (even) or 1 (odd)
                result = 0
                for digit in range(maxdigit + 1):
                    diff_next = diff + digit * possign
                    digitlim_next = digit == maxdigit and digitlim
                    result += dfs(i+1, diff_next, digitlim_next)
                return result

            return dfs(0, 0, True)

        return calc(high) - calc(low - 1)