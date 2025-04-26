class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @cache
        def dfs(rollsLeft, prevRollNumber, freqRollNumber): # O (n * 6 * max(rollMax))
            if freqRollNumber > rollMax[prevRollNumber - 1]:
                return 0

            if rollsLeft == 0:
                return 1
            res = 0
            for i in range(6):
                if i+1 == prevRollNumber:
                    res += dfs(rollsLeft - 1, i+1, freqRollNumber + 1)
                else:
                    res += dfs(rollsLeft - 1, i+1, 1)
            return res
            
            

        
        return dfs(n, -1, -1) % (10 ** 9 + 7)