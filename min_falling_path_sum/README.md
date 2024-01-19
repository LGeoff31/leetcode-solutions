Link to question: https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19

## Solution 1

Generate every possible sum for all the starting numbers by bfs'ings them all and updating the minimum sum

### Analysis

- Time Complexity: `O(m * 3^n)`
- Space Complexity: `O(m* 3^n)`

## Solution 2

Key Idea: the element at matrix[i][j] should be the smallest value to get their. Treat as 2-D DP problem.

### Analysis

- Time Complexity: `O(n*m)`
- Space Complexity: `O(n*m)`
