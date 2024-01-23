Link to question: https://leetcode.com/problems/pacific-atlantic-water-flow/

## Solution 1

Instead of going to every element and graph traversing in all 4 directions, you can cleverly optimize this. You know that all elements on the left and top rows are already connected with pacfic and all the right and bottom elements are on the atlantic. So do some backtracking, start from those and see which unique elements can be reached from all the pacific elements and vice versa. Then the ones which can reach both pacific and atlantic will be contained in both sets.

### Analysis

- Time Complexity: `O(n*m)`
- Space Complexity: `O(n*m)`
