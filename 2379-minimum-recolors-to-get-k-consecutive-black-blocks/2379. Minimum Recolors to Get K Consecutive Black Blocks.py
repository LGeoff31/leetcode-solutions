class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 1e9
        if len(blocks) == 1: return int(blocks[0] == "W")
        for i in range(len(blocks)):
            W = 0
            if i+(k-1) >= len(blocks):
                break
            for j in range(i, i+k):
                W += blocks[j] == "W"
            res = min(res, W)
        return res