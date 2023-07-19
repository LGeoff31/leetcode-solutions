Link to question: https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

## Solution 1

While there is a next node, if the next node and current node have the same value, set the next node equal to the one after that, otherwise increment the node to next

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
