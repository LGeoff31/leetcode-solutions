Link to question: https://leetcode.com/problems/house-robber/description/

## Solution 1

Key idea, dp[i] = max(dp[i-2] + nums[i], dp[i-1]), this works because dp[i-2] + nums[i] gives a valid answer since your skipping the (i-1 ) term giving one of the maximum results. The other one will simply be if the (i-1)th term is included, hence, you wouldn't be able to include the nums[i]. Those are the two that maximize so take the whichever is larger.

### Analysis 1

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
