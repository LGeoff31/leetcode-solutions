Link to question: https://leetcode.com/problems/squares-of-a-sorted-array/description/

## Solution 1

To calculate the ith number, you can derive a formula. for numbers below the ith number, the absolute value is not needed, it will simply be ith number - number previous. For numbers after, it will be number after - ith number, thus eliminating then need for abs. (taking advantage of the sorted array). Note, the ith number in the summation will occur (the number elements before it - number elements after it). The numbers before it will all be subtracted in the summation and the number after it will be added. Simply reduce the time needed by utilizing a prefix sum and that is the solution!

### Analysis

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

## Solution 2

Loop each number with each of the other numbers and sum the absolute differences

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(n)`
