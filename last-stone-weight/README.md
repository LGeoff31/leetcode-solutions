Link to question: https://leetcode.com/problems/last-stone-weight/

## Solution 1

Use a heap for a logn operation to determine the maximum value. Since python only supports min heaps aka extracting the minimum in a array in logn time, we can multiply every number in the array by -1 so we can extract technically the largest number since -8 will be extracted over -7 since it'll be now considered a minimum. Pop from the heap having the array as an argument and this will continiously update stones until it has a length of 1 or 0, break out the loop and return the first element if there is one, make sure to absolute value since it would all be negatives.

### Analysis

- Time Complexity: `O(nlogn)`
- Space Complexity: `O(n)`
