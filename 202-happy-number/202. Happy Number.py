class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def get_digit_square_sum(num):
            res = 0
            for c in str(num):
                res += int(c)**2
            return res

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_digit_square_sum(n)
        return True