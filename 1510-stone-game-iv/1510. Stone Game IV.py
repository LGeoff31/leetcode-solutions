class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dfs(remaining, alice_turn):
            if remaining == 0:
                return not alice_turn
            
            if alice_turn:
                res = False
                for i in range(1, ceil(sqrt(remaining)) + 1):
                    i_squared = i**2
                    if i_squared <= remaining:
                        res = res or dfs(remaining - i_squared, not alice_turn)
                return res
            else:
                res = True
                for i in range(1, ceil(sqrt(remaining)) + 1):
                    i_squared = i**2
                    if i_squared <= remaining:
                        res = res and dfs(remaining - i_squared, not alice_turn)
                return res


        return dfs(n, True)