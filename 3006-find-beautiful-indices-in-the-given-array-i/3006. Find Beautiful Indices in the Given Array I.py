class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        res = []
        for i in range(len(s) - len(a) + 1):
            if s[i: i+len(a)] == a:
                fullstring = s[max(0, i-k) : min(i+len(b)+k, len(s))]
                if b in fullstring:
                    res.append(i)
        return res