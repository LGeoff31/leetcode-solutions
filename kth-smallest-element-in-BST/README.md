Link to question: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

## Solution 1

Run a dfs through all nodes while appending to list, sort the list, return the (k-1)th element

### Analysis

- Time Complexity: `O(nlogn)`
- Space Complexity: `O(n)`

## Solution 2

Run a dfs in order, left to right, through all nodes while appending to list, sort the list, return the (k-1)th element

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
