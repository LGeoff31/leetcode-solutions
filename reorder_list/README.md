Link to question: https://leetcode.com/problems/reorder-list/

## Solution 1

Use tortoise and hair to determine the half way point in linked list. Reverse the secound half. Point the left node to the righted node and update left, then point the right to the left node and update right and this will continue to shrink down the the middle of the linked list until left == right, at which point you have reorederd the linked list as required :o

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
