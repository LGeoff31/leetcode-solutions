Link to question: https://leetcode.com/problems/move-zeroes/description/

## Solution 1

Traverses through linearly and swaps adjacent elements if the one on the left is a zero and the right is a non-zero. Continues this process until all zeros are to the right.

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(1)`

## Solution 2

Similar to Solution 1 except two pointers, one at a zero, then the other will linearly scan through the right of that zero pointer to find a non-zero, then swap

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

## Solution 3

Traverse through the array, if you come across a zero, remove it then append to end of the array

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
