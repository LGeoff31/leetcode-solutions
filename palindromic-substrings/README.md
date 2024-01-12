Link to question: https://leetcode.com/problems/palindromic-substrings

## Solution 1

Generate every possible substring and check if its a palindrome

### Analysis

- Time Complexity: `O(n^3)`
- Space Complexity: `O(1)`

## Solution 2

Loop through each of the characters and have a left and right pointer to expand outwards to check for palindromes. Note you have to do this for odd and even length so have two for loops.

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(1)`
