Link to question: https://leetcode.com/problems/unique-paths/

## Solution 1

BFS by computing every path and adding 1 to the result if the path is equal to the final destination (MLE)

### Analysis

- Time Complexity: `O(2^(n*m))`
- Space Complexity: `O(2^(n*m))`

## Solution 2

Recursively create sub-problems since the only moves and either right or down where the base case will be when the position is either 1 above or the left of the end. (TLE)

### Analysis

- Time Complexity: `O(2^(n*m))`
- Space Complexity: `O(n*m)`

## Solution 3

Same as solution 2 by cache with a 2 dimensional memoization dictionary to reduce repeated work

### Analysis

- Time Complexity: `O(n*m)`
- Space Complexity: `O(n*m)`
