class Solution:
    def partitionString(self, s: str) -> List[str]:
        visited = set()
        res = []
        curr = ""
        for i in range(len(s)):
            curr += s[i]
            if curr not in visited:
                visited.add(curr)
                res.append(curr)
                curr = ""
            

        return res