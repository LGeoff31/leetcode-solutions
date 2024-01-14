Link to question: https://leetcode.com/problems/determine-if-two-strings-are-close/

## Solution 1

This can't be solved intuitively. For this to occur, word1 and word2 must not have any characters where one has it but the other doesn't. Additionally, when tallying up the frequency for one of the words, there should never be a case where that frequency doesn't occur in the other one, as then the strings will never equal. If these cases are satisfied, it is possible to make the strings the same with operations 1 & 2, think about it!

### Analysis

- Time Complexity: `O(n * m)`
- Space Complexity: `O(n * m)`
