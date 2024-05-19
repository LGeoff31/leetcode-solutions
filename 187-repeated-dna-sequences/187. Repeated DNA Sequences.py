class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = set()
        res = []
        for i in range(len(s) - 10 + 1):
            substring = s[i:i+10]      
            if substring in visited:
                res.append(substring)
            else:
                visited.add(substring)      
        return list(set(res))
        