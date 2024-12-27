class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if 1 not in stones: return False
        indicies = {num: i for i, num in enumerate(stones)}
        # @cache
        print(indicies)
        visited = set()
        @cache
        def dfs(idx, curr, prevJump):
            print(idx, curr, prevJump)
            if idx == len(stones) - 1:
                return True
            if prevJump < 0: 
                return False
            if (idx, curr, prevJump) in visited:
                return False
            visited.add((idx, curr, prevJump))
            
            res = False
            if curr+prevJump-1 in indicies:
                res = res or dfs(indicies[curr+prevJump-1], curr+prevJump-1, prevJump-1)
            if curr+prevJump in indicies:
                res = res or dfs(indicies[curr+prevJump],curr+prevJump, prevJump)
            if curr+prevJump+1 in indicies:
                res = res or dfs(indicies[curr+prevJump+1], curr+prevJump+1, prevJump+1)
            return res
            
        return dfs(1, 1, 1)