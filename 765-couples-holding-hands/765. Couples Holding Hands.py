class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        res = 0
        for i in range(0, len(row), 2):
            match = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
            idx_match = row.index(match)
            if row[i+1] != match:
                row[i+1], row[idx_match] = row[idx_match], row[i+1]
                res += 1
        return res
