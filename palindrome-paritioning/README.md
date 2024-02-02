Link to question: https://leetcode.com/problems/palindrome-partitioning/

## Solution 1

Backtracking solution generating every possible partition and seeing if all the portions are palindrome.

- Do a DFS
- Base case: when the index is greater or equal length of string, that means all previous parts must've been palindromes and you got to the end so you can add the partition which contains them all to your result, note make sure to add a copy as partition will contiously change throughout
- Recursively call dfs on the next portion if its a plaindrome while increasing the index, also once you do a dfs call, pop from the partition to dfs on other possibilities

### Analysis

- Time Complexity: `O(2^n)`
- Space Complexity: `O(2^n)`
