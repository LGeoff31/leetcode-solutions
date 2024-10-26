from typing import List

class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(k)]

        for curr_city in range(n):
            dp[0][curr_city] = stayScore[0][curr_city]
            for start_city in range(n):
                if start_city != curr_city:
                    dp[0][curr_city] = max(dp[0][curr_city], travelScore[start_city][curr_city])

        for day in range(1, k):
            for curr_city in range(n):
                dp[day][curr_city] = dp[day - 1][curr_city] + stayScore[day][curr_city]
                
                for prev_city in range(n):
                    if prev_city != curr_city:
                        dp[day][curr_city] = max(dp[day][curr_city], dp[day-1][prev_city] + travelScore[prev_city][curr_city] )

        return max(dp[k-1])
