class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0: return False
        sideLength = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > sideLength:
            return False
        sides = [0] * 4
        def dfs(idx):
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for i in range(4):
                if matchsticks[idx] + sides[i] <= sideLength:
                    sides[i] += matchsticks[idx]
                    if dfs(idx+1):
                        return True
                    sides[i] -= matchsticks[idx]
            return False
                    
        return dfs(0)