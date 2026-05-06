class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        abcde
        caebd


        great

        dfs(gr) + dfs(eat)
        dfs(r) + dfs(g) + 


        """
        if len(s1) != len(s2):
            return False 
        @cache
        def dfs(a,b):
            if a == b:
                return True 
            
            if Counter(a) != Counter(b):
                return False 
            
            for i in range(1, len(a)):
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True 
                
                if dfs(a[:i], b[len(a) - i:]) and dfs(a[i:], b[:len(a) - i]):
                    return True

            return False 
               
        return dfs(s1, s2)
