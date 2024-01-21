Link to question: https://leetcode.com/problems/number-of-islands/

## Solution 1

Traverse through the 2d array, if its a 1, check for all adjacent 1's in all 4 directions (very important) but don't check if its already been check. Do this by continiously adding to a visited set

### Analysis

- Time Complexity: `O(n*m)`
- Space Complexity: `O(n*m)`
