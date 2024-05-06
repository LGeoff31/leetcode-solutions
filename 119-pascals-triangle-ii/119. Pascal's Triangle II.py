class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0: return [1]
        dp = [[] for _ in range(n+1)]
        dp[0] = [1]
        dp[1] = [1, 1]
        print(dp)
        for i in range(2, n+1):
            newArr = []
            newArr.append(dp[i-1][0])
            for j in range(1, len(dp[i-1])):
                newArr.append(dp[i-1][j] + dp[i-1][j-1])
            newArr.append(dp[i-1][-1])
            dp[i] = newArr

        print(dp)
        return dp[-1]
        