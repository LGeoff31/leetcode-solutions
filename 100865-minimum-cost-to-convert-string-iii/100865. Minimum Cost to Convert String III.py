class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == float('inf'): continue
            if source[i] == target[i]:
                dp[i+1] = min(dp[i], dp[i+1])

            # otherwise try applying a rule
            for (pattern, replacement), cost in zip(rules, costs):
                idx = 0
                if i + len(pattern) >= n+1:
                    continue
                if target[i: i + len(pattern)] != replacement:
                    continue 
                
                valid = True 
                cnt = 0
                for j in range(len(pattern)):
                    if pattern[j] == "*": cnt += 1
                    elif pattern[j] != source[i+j]:
                        valid = False 
                        break 
                    
                if valid:
                    dp[i+len(pattern)] = min(dp[i+len(pattern)], dp[i] + cost + cnt)
        return dp[len(source)] if dp[n] != float('inf') else -1
                    