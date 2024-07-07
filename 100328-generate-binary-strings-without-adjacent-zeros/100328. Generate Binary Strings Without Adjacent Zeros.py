class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.res = []
        def dfs(string, prev_was_one):
            if len(string) == n:
                self.res.append(string)
                return
            
            if prev_was_one:
                dfs(string + "0", False)
            dfs(string + "1", True)
        dfs("0", False)
        dfs("1", True)
        return self.res