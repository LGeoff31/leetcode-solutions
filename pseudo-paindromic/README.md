Link to question: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/?envType=daily-question&envId=2024-01-24

## Solution 1

Traverse by giving a set, if the you come across a value already in the set remove it since even numbers can be removed to check if palindrome, only condition is that you can't have more than 1 odd frequency character. DFS through each path so each set will contain all the elements in each path. 

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

