class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 1 + 2 + .. .+ 15 = 8 x 15 = 120
        lst = list(range(1, maxChoosableInteger + 1))
        if sum(lst) < desiredTotal:
            return False

        @cache
        def dfs(lst, remainingTotal):
            if lst[-1] >= remainingTotal:
                return True
            
            for i in range(len(lst)):
                if dfs(lst[:i] + lst[i+1 : ], remainingTotal - lst[i]) == False:
                    return True
            return False


        return dfs(tuple(lst), desiredTotal)

      