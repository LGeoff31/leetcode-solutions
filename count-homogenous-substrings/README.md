Link to question: https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description

## Solution 1

Discover a pattern for consecutive homogenous strings which adds the common arithmetic sum from 1 to n to count. Do this process while taking care of minor edge cases:

- Ensure the string is at minimum length 2
- Note, the comparison is with the current index, to next, and the last character will not be added to the result, so after loop, add to result depending on the two possibilities, the last character was a continuation of the last homogeneous substring or it was just a new character

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
