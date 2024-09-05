class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_dices = len(rolls) + n
        missing = mean*total_dices - sum(rolls)
        print(missing)
        val = missing // n
        remainder = missing % n
        print(val, remainder)
        if (remainder and 1+val > 6) or val > 6 or val < 1: return []
        a = []
        for i in range(n - remainder):
            a.append(val)
        for i in range(remainder):
            a.append(val + 1)
        return a

