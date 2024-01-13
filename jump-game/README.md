Link to question: https://leetcode.com/problems/jump-game/

## Solution 1

Backtracking bottom up algorithm. Start from the end and to see if a index can jump to the end, the condition i + nums[i] >= goal must be met and if so, move the goal closer to the start. If the goal eventually reaches the start, then a solution is found. Very helpful to backtrack rather than fronttrack because it heavily reduces the amount of possibilities to a linear scan.

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
