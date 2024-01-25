https://leetcode.com/problems/set-matrix-zeroes/

## Solution 1

Don't change anything just mark where all the 0's are first. Then mutate. Note, you can improve the space complexity to O(m + n) and time complexity to O(n \* m) by marking which rows and cols need to be turned to all zeros with a X mark.

### Analysis

- Time Complexity: `O(m * n)`
- Space Complexity: `O((m * n) * (m+n))`
