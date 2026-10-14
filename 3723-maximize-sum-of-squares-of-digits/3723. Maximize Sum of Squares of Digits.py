class Solution:
    def maxSumOfSquares(self, num: int, _sum: int) -> str:
        res = [0] * num

        full_nines = _sum // 9
        remainder = _sum % 9

        res = [9] * full_nines
        if remainder:
            res.append(remainder)
        remaining_length = num - len(res)
        res = res + [0] * remaining_length
        if len(res) > num: return ""
        return "".join(str(c) for c in res)
