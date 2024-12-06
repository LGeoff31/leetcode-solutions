class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        a = set(banned)
        res = 0
        curr = 0
        for i in range(1,n+1):
            if i in a:
                continue
            if curr + i <= maxSum:
                curr += i
                res += 1
            else:
                break
        return res
