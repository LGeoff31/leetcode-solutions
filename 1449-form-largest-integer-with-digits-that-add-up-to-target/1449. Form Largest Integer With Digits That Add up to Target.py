class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        dp = [""] + ["#"] * target
        
        for d in range(9, 0, -1):
            c = cost[d-1]
            for t in range(c, target+1):
                if dp[t-c] != "#":
                    candidate = dp[t-c] + str(d) 
                    if dp[t] == "#" or len(candidate) > len(dp[t]) or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate
        
        return dp[target] if dp[target] != "#" else "0"
