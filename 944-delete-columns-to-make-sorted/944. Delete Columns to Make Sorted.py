class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        rows, cols = len(strs), len(strs[0])

        for c in range(cols):
            lst = []
            for r in range(rows):
                lst.append((strs[r][c]))
            if lst != sorted(lst):
                res += 1
        return res