class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        size = k
        remainder = len(s) % k
        res = []    
        i = 0
        while i < len(s):
            if i+size <= len(s):
                res.append(s[i: i+size])
            else:
                res.append(s[i:] + fill * ((size - len(s[i:]))))
            i += size
        return res