Link to question: https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description

## Solution 1

If you have enough time to travel to endpoint using most efficient path, go diagonally until either x or y is reached, then go horz or vert to complete it, then you will def reach there in time

- Only exception is distance needed to move = 0 and t=1, since t=2 you can move right then back, t=3 u can go diagonally (essentailly 2 moves), then left and down, so any odd number can be offsetted by going diagonally

### Analysis

- Time Complexity: `O(1)`
- Space Complexity: `O(1)`
