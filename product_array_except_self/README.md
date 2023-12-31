Link to question: https://leetcode.com/problems/group-anagrams/submissions/1132761675/

## Solution 1

Loop through, remove the element and multiply all the others

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(n)`

## Solution 1

Create a prefix and postfix array. The ith element of the result will be the (i-1)ith element of the prefix array multiplied by the (i+1)th element of the postfix array. Math!

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
