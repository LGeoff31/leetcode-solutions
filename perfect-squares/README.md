Link to question: https://leetcode.com/problems/perfect-squares/?envType=daily-question&envId=2024-02-08

## Solution 1

Build up your dp array bottom up. To determine d[i], it will equal 1 + dp[i - perfect squares]

### Analysis

- Time Complexity: `O(n^3/2)`
- Space Complexity: `O(n)`

#
