Link to question: https://leetcode.com/problems/3sum/description/

## Solution 1

Sort the array first, traverse a pointer through the unique elements in the sorted array, at each iteration, put left pointer one after the current iteration, put right at end array, calculate the current threesum. If its positive, decrement right as it too large, if its negative increment left pointer, if it equates to 0, add to result list and also increment left counter to find other possible two sums, however, if the following nums[left] is the same as previous, incremet left since you don't want the result array to have duplicates.

### Analysis

- Time Complexity: `O(n^2)`
- Space Complexity: `O(n)`

## Solution 2

Brute force: 3 pointer to generate every tuple in the array, check if sum is zero. To remove duplicates, add a python set, and ensure the three numbers aren't in seen in that set, otherwise add to result array

### Analysis

- Time Complexity: `O(n^3)`
- Space Complexity: `O(n)`
