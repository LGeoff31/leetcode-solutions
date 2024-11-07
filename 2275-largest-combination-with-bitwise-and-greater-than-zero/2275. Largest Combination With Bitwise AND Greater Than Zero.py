class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            count = 0
            for num in candidates:
                if num & mask:
                    count += 1
            res = max(res, count)
        return res