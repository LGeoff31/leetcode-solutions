Link to question: https://leetcode.com/problems/first-missing-positive/

## Solution 1

Move the numbers value to the corresponding index place, if any of the index places aren't positive then that is the position where the missing index is. Beautiful way to reduce the space complexity to O(1) auxillary space

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
