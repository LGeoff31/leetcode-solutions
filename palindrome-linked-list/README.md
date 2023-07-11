Link to question: https://leetcode.com/problems/palindrome-linked-list/description/

## Solution 1

Converts Linked List into array and checks if the array is a palindrome, much simpler

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Solution 2

Utilizes two pointers, slow one reaches half way mark while fast reaches the end. Reverse the second half of the linked list aka slow onwards, then from the two endpoints of the entire linked list, traverse towards the center checking if the elements on both sides are equal.

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
