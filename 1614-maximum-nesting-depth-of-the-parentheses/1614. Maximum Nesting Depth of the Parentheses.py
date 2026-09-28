class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        net_open = 0
        for c in s:
            net_open += (1 if c == "(" else (-1 if c == ")" else 0))
            res = max(res, net_open)
        return res