Link to question: https://leetcode.com/problems/longest-repeating-character-replacement/description/

## Solution 1

Slidiing Window Problem

- Have left and right pointer, since at most k replacements, that means the number of replacements needed given any string in dictionary frequency format will be the sum of the values of the dic minus the max value in dic. Essentially, if this value becomes greater than k, you must slide your left pointer contioniously until the at most k distinctions is satisfied. Very fun problem.

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
