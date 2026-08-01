class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(l, r, isPlayerOne, currentScore):
            if r < l:
                return currentScore >= 0

            if isPlayerOne:
                res = False
                # CONSUME LEFT NUMBER
                res = res or dfs(l+1, r, not isPlayerOne, currentScore + nums[l] * (1 if isPlayerOne else -1))

                # CONSUMER RIGHT NUMBER
                res = res or dfs(l, r-1, not isPlayerOne, currentScore + nums[r] * (1 if isPlayerOne else -1))
                return res
            
            else:
                res = True 
                res = res and dfs(l+1, r, not isPlayerOne, currentScore + nums[l] * (1 if isPlayerOne else -1))

                # CONSUMER RIGHT NUMBER
                res = res and dfs(l, r-1, not isPlayerOne, currentScore + nums[r] * (1 if isPlayerOne else -1))
                return res 
        
        return dfs(0, len(nums) - 1, True, 0)


