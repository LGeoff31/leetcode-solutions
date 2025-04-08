class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        rows, cols = len(s2), len(s1)
        dp = [[0] * (cols+1) for _ in range(rows+1)]

        for c in range(1, cols+1):
            dp[0][c] = dp[0][c-1] + ord(s1[c - 1])
        for r in range(1, rows+1):
            dp[r][0] = dp[r-1][0] + ord(s2[r - 1])

        for c in range(1, cols+1):
            for r in range(1, rows+1):
                if s1[c - 1] == s2[r - 1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(ord(s2[r - 1]) + dp[r-1][c], ord(s1[c-1]) + dp[r][c-1])
        print(dp)
        return dp[rows][cols]
        # If all characters in s1 and not present in s2, return sum of both ASCII values

        # Brute force: generate all subsequences for s1 + s2, then find the ones unique and find the cost to get it there, O(2^n)

        # Note you CANNOT be gready -> Taking the longest common subsequence 

        # Dp[i][j] = ans for s1[i:] and s2[j:]

        # Key: if s1[i] == s2[i], then dp[i][j] = TOTAL_ASCII_SUM - dp[i+1][j+1] - ord(s1[i] + s2[i])
        # TOTAL_ASCII_SUM = 0
        # for letter in s1:
        #     TOTAL_ASCII_SUM += ord(letter)
        # for letter in s2:
        #     TOTAL_ASCII_SUM += ord(letter)
        # if not(sum(a in s2 for a,b in zip(s1,s2)) >= 1):
        #     return TOTAL_ASCII_SUM
        # print(ord("t"), ord("e"), TOTAL_ASCII_SUM)
        # dp = [[1e9] * len(s2) for _ in range(len(s1))]
        # for i in range(len(s1) - 1, -1, -1):
        #     for j in range(len(s2) -1, -1, -1):
        #         if j == len(s2) - 1:
        #             if s1[i] == s2[j]:
        #                 dp[i][j] = TOTAL_ASCII_SUM - 2*ord(s1[i])
        #             else:
        #                 if i+1 < len(s1):
        #                     dp[i][j] = min(dp[i][j], dp[i+1][j])
        #         elif i == len(s1) - 1:
        #             if s1[i] == s2[j]:
        #                 dp[i][j] = TOTAL_ASCII_SUM - 2*ord(s1[i]) 
        #             else:
        #                 if j+1 < len(s2):
        #                     dp[i][j] = min(dp[i][j], dp[i][j+1])
        #         else:
        #             if s1[i] == s2[j]:
        #                 dp[i][j] = min(dp[i+1][j+1] - 2*ord(s1[i]), TOTAL_ASCII_SUM - 2*ord(s1[i]))
        #             else:
        #                 dp[i][j] = min(dp[i+1][j], dp[i][j+1])
        # print(dp)
        # return dp[0][0]

