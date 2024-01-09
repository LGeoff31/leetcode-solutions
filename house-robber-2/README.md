Link to question: https://leetcode.com/problems/house-robber-ii/description/

## Solution 1

Very similar to House Robber 1. Except constraint that the dp array cannot include both the first and last since there neighbors. To resolve this issue, have two dp arrays.

- Calculate dp array for elements 0 to (n-1)
- Calculate dp array for elements 1 to n

- Take max between these two dp's

### Analysis 1

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
