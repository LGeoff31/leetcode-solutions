class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def meet_conditions(string):
            for i in range(1, len(string)):
                if pattern[i-1] == "I":
                    if string[i] <= string[i-1]:
                        return False 
                else:
                    if string[i] >= string[i-1]:
                        return False 
            return True
        res = ""
        def dfs(string):
            if len(string) > len(pattern) + 1: return
            if meet_conditions(string):
                if len(string) == 1 + len(pattern):
                    print('reached', string)
                    # res = string
                    return string
            
                for i in range(1, 10):
                    if str(i) not in string:
                        if dfs(string + str(i)):
                            return dfs(string + str(i))
            
        
        return dfs("")
        # return res

        