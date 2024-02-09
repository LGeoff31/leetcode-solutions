Link to question: https://leetcode.com/problems/largest-divisible-subset/?envType=daily-question&envId=2024-02-09

## Solution 1

Dp[i] = max(dp[i], 1 + dp[j]) where 0<=j less than i. Store max index and max length so you can traverse backwards and find the numbers that make up the max length subset.

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(n)`
