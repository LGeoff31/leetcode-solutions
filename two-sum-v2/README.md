Link to question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

## Solution 1

Two pointers left and right, if sum current two elements at pointers equals target, return, otherwise if larger, decrement right pointer, if smaller, increment left pointer, do this process until either pair is found or the left and right pointers overlap

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
