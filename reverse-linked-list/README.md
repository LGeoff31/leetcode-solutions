Link to question: https://leetcode.com/problems/reverse-linked-list/

## Solution 1

Converts Linked list into a array, reverses the array, converts back to a linked list

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Solution 2

Same as Solution 1 but the functons to transform linked list to array and vice versa are done recursively

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Solution 3

Uses two pointers, reverses the link between two consective nodes throughout the loop then returns the last head

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
