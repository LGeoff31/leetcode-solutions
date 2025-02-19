class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.lst = []

        def dfs(string):
            if len(string) == n:
                self.lst.append(string)
                return
            for c in ["a", "b", "c"]:
                if not string:
                    dfs(c)
                else:
                    if c != string[-1]:
                        dfs(string + c)
        dfs("")
        print(self.lst)
        if k-1 >= len(self.lst): return ""
        return sorted(self.lst)[k-1]
