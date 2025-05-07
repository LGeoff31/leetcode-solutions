from typing import List, Tuple

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> Tuple[int, int]:
        rows, cols = len(moveTime), len(moveTime[0])
        dp = [[(1e9, 0)] * cols for _ in range(rows)] 
        dp[0][0] = (0, 0)

        for c in range(1, cols):
            if dp[0][c - 1][0] < moveTime[0][c]:
                dp[0][c] = (moveTime[0][c] + 1, dp[0][c - 1][1] + 1) 
            else:
                dp[0][c] = (dp[0][c - 1][0] + 1, dp[0][c - 1][1] + 1)  
        
        # Fill in first column
        for r in range(1, rows):
            if dp[r - 1][0][0] < moveTime[r][0]:
                # Must wait
                dp[r][0] = (moveTime[r][0] + 1, dp[r - 1][0][1] + 1) 
            else:
                dp[r][0] = (dp[r - 1][0][0] + 1, dp[r - 1][0][1] + 1) 
        # Fill in the rest of the dp grid
        for r in range(1, rows):
            for c in range(1, cols):
                # Check up
                if dp[r][c - 1][0] < moveTime[r][c]:
                    new_time = moveTime[r][c] + 1
                    new_steps = dp[r][c - 1][1] + 1
                else:
                    new_time = dp[r][c - 1][0] + 1
                    new_steps = dp[r][c - 1][1] + 1
                dp[r][c] = (new_time, new_steps)

                # Check left
                if dp[r - 1][c][0] < moveTime[r][c]:
                    new_time = moveTime[r][c] + 1
                    new_steps = dp[r - 1][c][1] + 1
                else:
                    new_time = dp[r - 1][c][0] + 1
                    new_steps = dp[r - 1][c][1] + 1

                # Update dp[r][c] with the minimum time and corresponding steps
                if (new_time < dp[r][c][0]) or (new_time == dp[r][c][0] and new_steps < dp[r][c][1]):
                    dp[r][c] = (new_time, new_steps)

        # Continue adjusting dp grid until stable
        while True:
            stable = True
            for r in range(rows):
                for c in range(cols):
                    current_time, current_steps = dp[r][c]

                    # Check down
                    if c + 1 < cols:
                        if dp[r][c + 1][0] < moveTime[r][c]:
                            new_time = moveTime[r][c] + 1
                            new_steps = current_steps + 1
                        else:
                            new_time = dp[r][c + 1][0] + 1
                            new_steps = dp[r][c + 1][1] + 1

                        if new_time < current_time or (new_time == current_time and new_steps < current_steps):
                            dp[r][c] = (new_time, new_steps)
                            stable = False

                    # Check right
                    if r + 1 < rows:
                        if dp[r + 1][c][0] < moveTime[r][c]:
                            new_time = moveTime[r][c] + 1
                            new_steps = current_steps + 1
                        else:
                            new_time = dp[r + 1][c][0] + 1
                            new_steps = dp[r + 1][c][1] + 1

                        if new_time < current_time or (new_time == current_time and new_steps < current_steps):
                            dp[r][c] = (new_time, new_steps)
                            stable = False

                    # Check up
                    if c - 1 >= 0:
                        if dp[r][c - 1][0] < moveTime[r][c]:
                            new_time = moveTime[r][c] + 1
                            new_steps = current_steps + 1
                        else:
                            new_time = dp[r][c - 1][0] + 1
                            new_steps = dp[r][c - 1][1] + 1

                        if new_time < current_time or (new_time == current_time and new_steps < current_steps):
                            dp[r][c] = (new_time, new_steps)
                            stable = False

                    # Check left
                    if r - 1 >= 0:
                        if dp[r - 1][c][0] < moveTime[r][c]:
                            new_time = moveTime[r][c] + 1
                            new_steps = current_steps + 1
                        else:
                            new_time = dp[r - 1][c][0] + 1
                            new_steps = dp[r - 1][c][1] + 1

                        if new_time < current_time or (new_time == current_time and new_steps < current_steps):
                            dp[r][c] = (new_time, new_steps)
                            stable = False

            # Break out of the loop if no changes were made
            if stable:
                break

        print(dp)  # Print the final dp state
        return dp[-1][-1][0]  # Return (min_time, steps) for dp[-1][-1]