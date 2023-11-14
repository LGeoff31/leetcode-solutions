Link to question: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

## Solution 1

Two pointers, when the two pointers hit the same character, check how many elements are between them and thats how many 3-digit palindromes can be made. Use set to eliminate any duplicates.

### Analysis

- Time Complexity: `O(n^3)`
- Space Complexity: `O(n)`

## Solution 1

Loop through with a pointer representing the middle character of the 3-digit palnidrome, keeping track of all elements to the left and right of that current pointer. The # palindromes that can be made are the # of same characters between the elements in left and right, of course eliminating duplicates with a set. Nice one way scan solution.

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
