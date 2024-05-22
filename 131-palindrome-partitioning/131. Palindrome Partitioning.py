class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    partition.append(s[i:j+1])
                    dfs(1+j)
                    partition.pop()
    
        dfs(0)
        return res
        