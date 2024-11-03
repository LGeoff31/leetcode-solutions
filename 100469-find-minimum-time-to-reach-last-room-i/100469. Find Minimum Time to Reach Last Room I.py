from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        dp = [[1e9] * cols for _ in range(rows)]

        # Fill in initial spot
        dp[0][0] = 0

        # Fill in first row
        for c in range(1, cols):
            if dp[0][c - 1] < moveTime[0][c]:
                # Must wait
                dp[0][c] = moveTime[0][c] + 1
            else:
                dp[0][c] = dp[0][c - 1] + 1
        
        # Fill in first column
        for r in range(1, rows):
            if dp[r - 1][0] < moveTime[r][0]:
                # Must wait
                dp[r][0] = moveTime[r][0] + 1
            else:
                dp[r][0] = dp[r - 1][0] + 1
        
        # Fill in the rest of dp grid
        for r in range(1, rows):
            for c in range(1, cols):
                # Check up
                if dp[r][c - 1] < moveTime[r][c]:
                    dp[r][c] = moveTime[r][c] + 1
                else:
                    dp[r][c] = dp[r][c - 1] + 1
                # Check left
                if dp[r - 1][c] < moveTime[r][c]:
                    dp[r][c] = min(dp[r][c], moveTime[r][c] + 1)
                else:
                    dp[r][c] = min(dp[r][c], dp[r - 1][c] + 1)

        # Continue adjusting dp grid until stable
        while True:
            stable = True
            for r in range(rows):
                for c in range(cols):
                    current_time = dp[r][c]

                    # Check down
                    if c + 1 < cols:
                        new_time = (moveTime[r][c] + 1) if dp[r][c + 1] < moveTime[r][c] else (dp[r][c + 1] + 1)
                        if new_time < current_time:
                            dp[r][c] = new_time
                            stable = False
                    
                    # Check right
                    if r + 1 < rows:
                        new_time = (moveTime[r][c] + 1) if dp[r + 1][c] < moveTime[r][c] else (dp[r + 1][c] + 1)
                        if new_time < current_time:
                            dp[r][c] = new_time
                            stable = False
                    
                    # Check up
                    if c - 1 >= 0:
                        new_time = (moveTime[r][c] + 1) if dp[r][c - 1] < moveTime[r][c] else (dp[r][c - 1] + 1)
                        if new_time < current_time:
                            dp[r][c] = new_time
                            stable = False
                    
                    # Check left
                    if r - 1 >= 0:
                        new_time = (moveTime[r][c] + 1) if dp[r - 1][c] < moveTime[r][c] else (dp[r - 1][c] + 1)
                        if new_time < current_time:
                            dp[r][c] = new_time
                            stable = False

            # Break out of the loop if no changes were made
            if stable:
                break

        print(dp)
        return dp[-1][-1]
