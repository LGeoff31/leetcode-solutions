class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = []
        def dfs(currString):
            if len(currString) == n:
                self.res.append(currString)
                return
            
            for option in ["a", "b", "c"]:
                if not currString:
                    dfs(currString + option)
                elif option != currString[-1]:
                    dfs(currString + option)
        
        dfs("")
        self.res.sort()
        print(self.res)
        if k-1 < len(self.res):
            return self.res[k-1]
        return ""