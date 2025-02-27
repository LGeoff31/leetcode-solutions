class Solution:
    def findDerangement(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        """
        The number of permutations is just n!, but we need a select portion so our ans <= n!
        [1,2,3] -> Success
        [2,1,x] -> Fails 
        
        [3,1,2] -> Success
        [3,x,x] -> Fails

        _[2,3] _[1,3] _[1,2]

        dp = [2, 3, 0]
        {
            2:1, 
            3:2,
            1:1
        }
        """
        prev1 = 0
        prev2 = 1
        if n == 1: return 0
        for i in range(2, n):
            tmp = prev2
            prev2=(i) * (prev1+prev2) % MOD
            prev1=tmp
        return prev2 % MOD