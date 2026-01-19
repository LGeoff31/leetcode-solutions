class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        start = s[:10]
        seen.add(start)

        for i in range(10, len(s)):
            start = start[1:] + s[i]
            if start in seen:
                res.add(start)
            
            seen.add(start)

        return list(res)