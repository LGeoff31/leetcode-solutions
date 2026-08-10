class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        memo = [-1] * (n + 1)
        
        def dfs(i):
            if i == n:
                return 0
            if memo[i] != -1:
                return memo[i]
            nxt = dfs(i + 1)
            if nxt < m and word1[i] == word2[m - nxt - 1]:
                res = nxt + 1
            else:
                res = nxt
            memo[i] = res
            return res
        
        dfs(0)  # fills memo[0..n-1] via the recursive chain
        dp = memo
        dp.append(0)  # dp[n] = 0, though memo already sized n+1
        
        # Greedy construction pass
        ans = []
        j = 0
        changed = False
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and dp[i + 1] >= m - j - 1:
                # skip/change word1[i] to word2[j]
                ans.append(i)
                j += 1
                changed = True
        
        return ans if j == m else []